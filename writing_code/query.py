import pandas as pd
from datetime import *
import requests

DATE_FORMAT = '%m/%d/%Y'
MIN_YEAR = 25

user_data = pd.read_csv("writing_code/user_data.csv")

user_data["BIRTH_DATE"] = pd.to_datetime(user_data["BIRTH_DATE"], format=DATE_FORMAT)

# 1. Write an SQL query that selects all records from the USER_DATA table above 
#    where SENT is 'N' and the BIRTH_DATE is more than 25 years ago.
filtered_user_data = user_data.loc[(user_data['SENT'] == 'N') & (date.today().year - user_data['BIRTH_DATE'].dt.year > MIN_YEAR)]

# End Result
print(filtered_user_data)

print("-----------------------------")

# 2. Write a function that takes a url and an associative array. The function should send a GET request to the
#    URL, passing the associative array as the form data. If the request returns a 200 status then the response
#    content should be returned; otherwise, an error should be thrown.
#

def send_get_request(url, formData):
    response = requests.get(url, params=formData)
    if response.status_code == 200:
        return response.content
    else:
        response.raise_for_status()
  


print("-----------------------------")

# 3. Write a function that takes a filename and an array. The function should join the values in the array with
#    commas and append it to the end of the file.
#

def append_array_to_file(filename, arr):
    with open(filename, 'a') as f:
        f.write(',')
        f.write(','.join(map(str, arr)))

test = ['one', 'two', 'three', 'four']

append_array_to_file('writing_code/array.txt', test)

# End Result
file = open('writing_code/array.txt', 'r')
print(file.read())
file.close()

print("-----------------------------")

# 4. Write a recursive function that takes an array. The function should return a new array that 
#    is the reverse of the original array.
#

def reverse(arr):
    if len(arr) <= 1:
        return arr
    else:
        return [arr[-1]] + reverse(arr[:-1])

test = ['one', 'two', 'three', 'four']

print(test)
# End Result
print(reverse(test))

print("-----------------------------")

