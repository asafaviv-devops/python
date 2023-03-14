filename = 'Desktop\python\movies.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.strip())
print("\n_______________________\n")

poped_movies = lines.pop()

for line in lines:
    print(line.strip())
print("\n_______________________\n")
sorted_list = lines.sort()

for line in lines:
    print(line.strip())
    