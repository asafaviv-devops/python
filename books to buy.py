def books_avaliable(*books):
    for book in books:
        books_in_stocks = "The following title is avaliable to buy" + book.title() 
        print(books_in_stocks)

avaliable = ['elon musk','the everything store','the growth']
books_avaliable(avaliable)