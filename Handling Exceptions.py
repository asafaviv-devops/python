### The Else block
print("please enter to numbers to be divided? ")
print('Enter "q" to quit')

while True:
    first_number = input("\n First Number: ")
    if first_number == 'q':
        break
    
    second_number = input('Second Number ')

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("you can't divide by 0!")
    else:
        print(answer)
