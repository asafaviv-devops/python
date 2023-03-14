### Making a list from a file
filename = 'Desktop\python\movies.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.strip())