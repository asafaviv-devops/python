### creating a class
class Book():
    def __init__(self, name, price, publisher):
        self.name= name
        self.price = price
        self.publisher = publisher

     def hardback(self):
        print(self.name.title + "is hardback book")

    def softback(self):
        print(self.name.title + "is a softback book")
    
    def ebook(self):
        print(self.name.title() + " is an ebook")