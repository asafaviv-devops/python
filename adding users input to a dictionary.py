### Adding user input to a dictionary
from timeit import repeat


rental_prop = {}
rental_open = True
while rental_open == True:
    username = input("\nWhat is your name")
    rental_property = input("what is the address?") 
    rental_properties[username] = rental_property
    repeat = input