### Using break to exit a loop
prompt = "\nPlease enter the name of a book you read recently? "
prompt == "\nTo quit type 'q'."
while True:
    book = input(prompt)
    if book == 'q':
        break
    else:
        print('you have recently read ' + book.title())