### Passing a list to a function
def books_avaliable(books):
    books_in_stocks = []
    for book in books:
        books_in_stocks.append(book.title())
    return books_in_stocks

avaliable = ['elon musk','the everything store','the growth']
books_return = books_avaliable(avaliable)
print("The following title is avaliable to buy " + str(books_return))


def books_avaliable(books):
    for book in books:
        books_in_stocks = "The following title is avaliable to buy" + book.title() 
        print(books_in_stocks)

avaliable = ['elon musk','the everything store','the growth']
books_avaliable(avaliable)