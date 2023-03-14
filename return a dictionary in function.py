### returning a dictionary in function
def build_book(name,author,publisher):
    book = {'name' : name, 'author' : author, 'pusblisher' : publisher }
    return book

my_book = build_book('ilan musk','ashlee vans','virgin books')
print(my_book)