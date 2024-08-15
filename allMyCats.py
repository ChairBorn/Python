catNames = []
while True:
    print('Enter the name of the cat ' + str(len(catNames) + 1) + '(Or enter nothing to stop): ') # Add the name to an empty list
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # Concatenate the list with the name we got
print('The cat names are:')
for name in catNames:
    print(' ' + name)