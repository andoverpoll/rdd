import bs4
from urllib.request import Request, urlopen
import random

numbers = []

for page in range(1, 104):
    url = 'https://localcallingguide.com/lca_prefix.php?page=' + str(page) + '&npa=603'
    print(page)
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read()
    soup = bs4.BeautifulSoup(html, 'html.parser')
    table = soup.find('table')
    t_body = table.find('tbody')
    rows = t_body.find_all('tr')

    for row in rows:
        area_code = row.find('td', attrs={'headers': 'npanxx'}).find('a').text
        block = row.find('td', attrs={'headers': 'block'}).text
        if area_code and block.isdigit():
            nums = []
            blocked = "+1" + area_code[:3] + area_code[4:] + block
            for i in range(50):
                new_num = blocked + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
                while new_num in nums:
                    new_num = blocked + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
                nums.append(new_num)
            numbers.append(nums)



with open('number_list.csv', 'w') as f:
    for number in numbers:
        f.write(','.join(number) + '\n')