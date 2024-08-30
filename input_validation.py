import pyinputplus as pyip

responseNum = pyip.inputNum() # Accepts only numbers as input
responseStr = pyip.inputStr() # Accepts only strings as input
responseYesNo = pyip.inputYesNo() # Accepts only 'yes' or 'no' as input
responseMenu = pyip.inputMenu(['a', 'b', 'c']) # Accepts only 'a', 'b', or 'c' as input