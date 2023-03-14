### using While loop in function
def get_format_name(first_name,last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print('\nWhat is your name? ')
    print('press q at any time to quit this program')
    first_name = input('First Name: ')
    last_name = input("Last Name: ")
    if first_name == 'q' or last_name == 'q':
        break 
    else:
        formatted_name = get_format_name(first_name,last_name)
        print('Hello ' + formatted_name)