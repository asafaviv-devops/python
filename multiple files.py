def word_count(name_of_file):
    try:
        with open(name_of_file) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        message = 'Sorry the file ' + name_of_file + ' cannot be found'
        print(message)
    else:
        words = contents.split()
        number_words = len(words)
        print("The file " + name_of_file + " has " + str(words) + str(number_words) + ' words')



filenames = [filepath]
for filename in filenames:
    word_count(filename)

filepath = 'Desktop\\python\\books.txt'
word_count(filepath)