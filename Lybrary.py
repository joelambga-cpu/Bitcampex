class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def checkout(self):
        if self.available:
            self.available = False
            return True
        else:
            return False

    def return_book(self):
        self.available = True

    def display_info(self):
        print(
            f"Title: {self.title}\nAuthor: {self.author}\nAvailable: {'Yes' if self.available else 'No'}"
        )


book1 = Book("Dracula", "Bram Stocker")
book2 = Book("Frankenstein", "Mary Shelley")
book3 = Book("1984", "George Orwell")
books = [book1, book2, book3]
for book in books:
    book.display_info()
