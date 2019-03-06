import datetime

class Book:
    def __init__(self, title, author="James Patterson", isbn="0", color="Default", year="", numPages=0):
        self.author = author
        self.title = title
        self.isbn = isbn
        self.color = color
        self.year = ""
        if not year:
            now = datetime.datetime.now()
            self.year = now.year
        else:
            self.year = year
        self.currentPage = 0
        self.numPages = numPages

        
    def description(self):
        return f"Book: {self.author}, {self.title}, {self.isbn}, {self.color}, {self.year}"

# create a book object with arguments for title, [author], [isbn], [color], [year], [numPages]
book1 = Book("DB Illuminated", "Urban", "234", "Blue", 2020, 300)
book2 = Book("HTML & CSS", "Murach", null, "Default")
book3 = Book("The Programming Mystery")
book1.title = "Databases Illuminated"

print(book1.description())
print(book2.description())
print(book3.description())
