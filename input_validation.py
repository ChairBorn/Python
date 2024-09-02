import pyinputplus as pyip

responseNum = pyip.inputNum() # Accepts only numbers as input
responseStr = pyip.inputStr() # Accepts only strings as input
responseYesNo = pyip.inputYesNo() # Accepts only 'yes' or 'no' as input
responseMenu = pyip.inputMenu(['a', 'b', 'c']) # Accepts only 'a', 'b', or 'c' as input
responseChoice = pyip.inputEmail() # Accepts only email addresses as input
responsePath = pyip.inputFilepath() # Accepts only file paths as input

response = pyip.inputNum('Enter a number: ', min=1, lessThan=100) # Prompts user to enter a number