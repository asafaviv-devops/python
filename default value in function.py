### default values in function
def book_description(author_name, book_type='non-fiction'):
    print("\nThis book is " + book_type )
    print("The Author of this book is " + author_name)

book_description('ashlee vance')
book_description('ashlee vance',book_type='fiction')
book_description('ashlee vance','fiction')
