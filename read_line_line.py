### Reading file line by line
filename = 'Desktop\python\movies.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.strip())