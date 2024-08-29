import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') # Parentheses are used to group the area code and main number, r stands for raw string
mo = phoneNumRegex.search('My number is 322-444-4567.')
area_code, main_number = mo.groups() # mo.groups() returns a tuple
print('Phone number found: ' + 'Area code: ' + area_code + ', Main number: ' + main_number)

begins_num = re.compile(r'^\d+') # ^ means the string must begin with a number
print(begins_num.search(r'(12 gates), (table with 10 chairs)')) # Returns 12