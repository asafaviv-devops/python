### Writing multiple lines to a file and using append
message = input("What is your favorite film: ")
print(message.title())

filename = 'Desktop\python\\film.txt'

with open(filename, 'a') as file_object:
    file_object.write(message + "\n")