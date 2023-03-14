def  word_count(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()

    except FileNotFoundError:
        pass

    else:
        words = contents.split()
        number_words = len(words)
        print("The file" + filename + " has " + str(number_words) + " words" )

filenames = ['Desktop\python\\books.txt','agfdgf.txt']
for filename in filenames:
    word_count(filename)
            