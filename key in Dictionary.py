### Using a key to get a value
### Create a Dictionary of terms
terms = {'variable' : 'represent a a value stored in memory','string' : 'Sequance of characters'}

if 'float' in terms:
    print('I know what a float is')
else:
    print('I don\'t know what it is')


print(terms['variable'])


terms={}
terms['variable'] = 'Represents to a value stored in memory'
terms['integer'] = 'a Whole number'
print(terms['variable'])
print(terms['integer'])
print(terms)
