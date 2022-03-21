#Make sure these settings are correct before running.
USER_ID = 'USER_ID'
API_KEY = 'API_KEY'
INPUT_FILENAME = 'number_list.csv'
OUTPUT_FILENAME = 'valid_numbers.txt'
COLUMNS_TO_RUN = 22
INITIAL_CALLS_REMAINING = 100000
INITIAL_VALID_NUMBERS = 0
START_COLUMN = 0
TARGET_SAMPLE_SIZE = 30000

import csv
from urllib import request, parse
import json

numbers_array = []
valid_numbers = []
url = 'https://neutrinoapi.net/phone-validate'

with open('number_list.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        numbers_array.append(row)

calls = 0
col = START_COLUMN

while col < COLUMNS_TO_RUN + START_COLUMN and len(valid_numbers) + INITIAL_VALID_NUMBERS < TARGET_SAMPLE_SIZE:
    for row in numbers_array:
        params = {
          'user-id': USER_ID,
          'api-key': API_KEY,
          'number': row[col]
        }
        calls+=1
        postdata = parse.urlencode(params).encode()
        req = request.Request(url, data=postdata)
        response = request.urlopen(req)
        result = json.loads(response.read().decode("utf-8"))
        if result["valid"]:
            if result["type"] != "premium-rate" and result["type"] != "toll-free" and result["type"] != "voip":
                valid_numbers.append(row[col])
    col+=1

with open(OUTPUT_FILENAME, "a") as file_object:
    for number in valid_numbers:
        file_object.write(number + '\n')

println("Calls remaining: " + str(INITIAL_CALLS_REMAINING - calls))
println("Next start column: " + str(col))
println("Total valid numbers: " + str(len(valid_numbers) + INITIAL_VALID_NUMBERS))
println("Sample achieved: " + str((len(valid_numbers) + INITIAL_VALID_NUMBERS))>=TARGET_SAMPLE_SIZE)