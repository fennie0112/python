class Book:
    def __init__(self):
        self.__title = ""
        self.__author = ""

    def set_data(self, title, author):
        self.__title = title
        self.__author = author

    def get_data(self):
        print("Title:", self.__title)
        print("Author:", self.__author)


b1 = Book()

b1.set_data("Python", "John")
b1.get_data()