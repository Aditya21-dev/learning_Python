# Library Management System (Single File OOPS Program)

class LibraryItem:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__available = True   # Encapsulation (Private Variable)

    def borrow_item(self):
        if self.__available:
            self.__available = False
            print(f"{self.title} has been borrowed.")
        else:
            print(f"{self.title} is currently not available.")

    def return_item(self):
        self.__available = True
        print(f"{self.title} has been returned.")

    def display_info(self):
        status = "Available" if self.__available else "Not Available"
        print("Title:", self.title)
        print("Author:", self.author)
        print("Status:", status)


# Child Class 1
class Book(LibraryItem):
    def __init__(self, title, author, genre):
        super().__init__(title, author)
        self.genre = genre

    def display_info(self):   # Method Overriding
        super().display_info()
        print("Genre:", self.genre)


# Child Class 2
class Magazine(LibraryItem):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.issue_number = issue_number

    def display_info(self):   # Method Overriding
        super().display_info()
        print("Issue Number:", self.issue_number)


# -------- Main Program --------

item1 = Book("The Alchemist", "Paulo Coelho", "Fiction")
item2 = Magazine("Tech Today", "Editorial Team", 45)

print("\n--- Book Details ---")
item1.display_info()
item1.borrow_item()
item1.display_info()
item1.return_item()

print("\n--- Magazine Details ---")
item2.display_info()
item2.borrow_item()
item2.display_info()