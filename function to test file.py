from test_code import get_formated_name

print("Enter 'q' to quit this program.")
while True:
    first = input("\n Please enter your first name: ")
    if first == 'q':
        break
    last = input("\n Please your last name: ")
    if last == 'q':
        break
    formatted_name = get_formated_name(first,last)
    print('your name is ' + formatted_name)