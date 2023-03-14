### Writing to an empty file
filename = 'Desktop\python\program.txt'
with open(filename, 'w') as file_object:
    file_object.write("Hello My name is Asaf")
    