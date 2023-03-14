### edit && delete values in dictionary
terms = {'integer' : 'is a number that contain a decimal place'}
print('integer ' + terms['integer'])
terms = {'integer' : 'A Whole number','String' : 'a sequance of charcters'}
del terms['integer']
print(terms)
terms['integer'] = 'decimal'
print(terms)
terms['float'] = 'float'
print(terms)
