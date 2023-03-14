### using list in a dictionary
my_car = {
    'Type' : 'standard for saloon',
    'extras' : ['alloy wheels','climate control','leather heated seats']
}
print('the car you orderd is a ' + my_car['Type'] + ' with the following extras:')
for extra in my_car['extras']:
    print(extra)