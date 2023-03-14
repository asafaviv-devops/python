def books_avaliable(*books):

    for book in books:
        books_in_stocks = "The following title is avaliable to buy " + str(book)
        print(books_in_stocks)
