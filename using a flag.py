### using a flag to stop a program
prompt = "Enter 'q' to end this program"
prompt +="\nWhat is your name?\n"
## Set or flage to true
active = True
while active:
    message = input(prompt)
    if message =='q':
        active = False
    else:
        print(message)