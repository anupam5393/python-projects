"""
Library Management system
"""

import datetime as dt


class Library:
    donated_books = dict()
    books = dict()
    borrowed_books = dict()

    def __init__(self, name, list_of_books):
        self.name = name
        for book in list_of_books:
            self.books.update({book.title(): {'available': 1}})

    def display_books(self):
        if len(self.books) != 0:
            print(f"\n\t\t{'List of the books'.center(50, '-')}")
            print(f"\t\t{'Book Name'.ljust(35, ' ')}{'Availability'.rjust(15, ' ')}\n")
            for book in self.books.keys():
                print(f"\t\t{book.ljust(35, ' ')}"
                    f"{'Yes'.rjust(15, ' ') if self.books[book]['available'] else 'No'.rjust(15, ' ') }")
        else:
            print(f'\n\t\tNo Books available!')

    def show_donated_books(self):
        if len(self.donated_books) != 0:
            print(f"\n\t\t{'List of books from Donations'.center(50, '-')}")
            print(f"\n\t\t{'Donator'.ljust(20, ' ')}{'Book Name'.rjust(30, ' ')}")
            for donator, book in self.donated_books.items():
                print(f"\t\t{donator.ljust(20, ' ')}{book.rjust(30, ' ')}")
        else:
            print(f"\n\t\tNo Donations Yet !!")

    def lend_book(self):
        borrower = str(input(f'\n\t\tEnter Borrower Name: '))
        self.display_books()
        book_name = str(input(f"\n\t\tName of the book to borrow/Check Status: ")).title()
        if book_name in list(map(lambda x: x.title(), self.books.keys())):
            if self.books[book_name]['available'] == 1:
                return_date = dt.datetime.strftime((dt.datetime.today() + dt.timedelta(days=7)), '%d-%m-%Y')
                self.books[book_name]['available'] = 0
                self.borrowed_books.update({book_name: {'borrower': borrower, 'blocked_till': return_date}})
                self.books[book_name]['blocked_till'] = return_date
                print(f"\n\t\tCongratulations you got it! Please return it on {return_date} :)")
            else:
                print(f"\n\t\tSorry currently this book is borrowed by {self.borrowed_books[book_name]['borrower']} "
                      f"and will be available on {self.borrowed_books[book_name]['blocked_till']}")
        else:
            print(f"\n\t\t:( Sorry, No Such Book Exist with us!")

    def return_book(self):
        lender_name = str(input(f'\n\t\tEnter the name by which you borrowed the book: '))
        book_name = str(input(f'\t\tName of the book you are returning: ')).title()
        if book_name in self.borrowed_books:
            self.borrowed_books.pop(book_name)
            self.books[book_name].pop('blocked_till')
            self.books[book_name]['available'] = 1
            print(f"\n\t\tThankyou for returning book.!!")
        else:
            print(f'\n\t\tNo such book is borrowed!!')

    def add_book(self):
        book_name = str(input(f'\n\t\tEnter the book Name: '))
        self.books.update({book_name.title(): {'available': 1}})

    def donate_book(self):
        book_name = str(input(f'\n\t\tEnter book name: '))
        donator = str(input(f'\t\tEnter Donator name: '))
        self.donated_books[donator] = book_name
        self.books.update({book_name.title(): {'available': 1}})

    def show_borrowed_books(self):
        if len(self.borrowed_books) != 0:
            print(f"\n\t\t{'List of lent books'.center(50, '-')}")
            print(f"\t\t{'Book Name'.ljust(35, ' ')}{'Borrowed By'.ljust(15, ' ')}{'Return Date'.ljust(15, ' ')}\n")
            for book in self.borrowed_books.keys():
                print(f"\t\t{book.ljust(35, ' ')}{self.borrowed_books[book]['borrower'].ljust(15, ' ')}{self.borrowed_books[book]['blocked_till'].ljust(15, ' ')}")
        else:
            print(f"\n\t\tNo books are lent.")

    def __str__(self):
        message = f'Welcome to {self.name}'
        return f"\t\t{message.center(50, ' ')}"


books_list = ['Cup of tea', 'Sultan', 'Bill Gates', 'Warren Baffet', 'Untold Story']
library = Library(str(input(f"\n\t\tEnter your Library Name: ")), books_list)

menu = '''
        ----------Menu----------
        1- Add book
        2- Display all Books
        3- Donate Book
        4- Display Donated Books
        5- List of lent books
        6- Lend Book
        7- Return Book
        8- Exit
'''

print(library)

while(1):
    print(menu)
    choice = int(input(f'\n\t\tEnter your choice: '))
    if(choice == 1):
        library.add_book()
    elif(choice == 2):
        library.display_books()
    elif(choice == 3):
        library.donate_book()
    elif(choice == 4):
        library.show_donated_books()
    elif(choice == 5):
        library.show_borrowed_books()
    elif(choice == 6):
        library.lend_book()
    elif(choice == 7):
        library.return_book()
    elif(choice == 8):
        exit()
    else:
        print(f'\n\t\tInvalid Choice!!')

