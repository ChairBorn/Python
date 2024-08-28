import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 322-444-4567.')
area_code, main_number = mo.groups() # mo.groups() returns a tuple
print('Phone number found: ' + 'Area code: ' + area_code + ', Main number: ' + main_number)