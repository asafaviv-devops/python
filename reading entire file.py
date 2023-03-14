### Read to entire file with path
filename = 'Desktop\python\movies.txt'
with open(filename) as file_object:
    contents = file_object.read()
    print(contents)