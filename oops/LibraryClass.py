class Library:

    def __init__(self, library_name, list_of_books):

        self.library_name = library_name
        self.list_of_books = list_of_books
        self.book_owner = {'': ''}

    def lend(self, bookName, ownerName):

        if (bookName in self.book_owner):

            print(
                f"Sorry, the book is already borrowed by {self.book_owner[bookName]}")
        else:
            self.book_owner[bookName] = ownerName
            print("Book borrowed successfully.")

    def returnBook(self, bookName):

        del self.book_owner[bookName]
        print("Book returned successfully.")

    def add_books(self, new_books):

        self.list_of_books.extend(new_books)
        print("Books added successfully")

    def discard_books(self, books):
        for i in books:
            self.list_of_books.remove(i)
        print("Books discarded successfully")

    def display(self):

        print("\nBooks in library : ", ", ".join(self.list_of_books))


if __name__ == "__main__":
    print("\tWelcome to the best library service.\n\n")

    library = input("Enter the library name: ")
    books = input("Enter the books names separated by a comma: ")
    selectedLibrary = library
    list_of_librarys = [library]

    exec("%s = Library('%s',%s)" %
         (library, library, books.strip().split(',')))

    print("""\nEnter following commands to work through...\n~Enter 0 to create a new library.\n\n~Enter 1 to display all books\n~Enter 2 to lend book to someone.\n~Enter 3 to return book from someone.\n~Enter 4 to add new books.\n~Enter 5 to discard books.\n~Enter 6 to switch to next library.""")
    while True:
        print("\nselected library : ", selectedLibrary)
        command = input("\nEnter command : ")
        if command == "1":
            exec("%s.display()" % (selectedLibrary))
        elif command == "2":
            bookname = input("Enter the book name: ")
            ownername = input("Enter the name of borrower: ")
            exec("%s.lend('%s','%s')" % (selectedLibrary, bookname, ownername))
        elif command == "3":
            bookname = input("Enter the returned book name: ")
            exec("%s.returnBook('%s')" % (selectedLibrary, bookname))
        elif command == "4":
            books = input("Enter the books names separated by a comma: ")
            exec("%s.add_books(%s)" %
                 (selectedLibrary, books.strip().split(",")))
        elif command == "5":
            books = input(
                "Enter the books names which you want to discard separated by a comma: ")
            exec("%s.discard_books(%s)" %
                 (selectedLibrary, books.strip().split(",")))
        elif command == "0":
            library = input("Enter the new library name: ")
            books = input(
                "Enter the books in new library separated by a comma: ")
            exec("%s = Library('%s',%s)" %
                 (library, library, books.strip().split(',')))
            selectedLibrary = library
            list_of_librarys.append(library)
        elif command == "6":
            for index, j in enumerate(list_of_librarys):
                print(f"Enter {index} to select {j}")
            selectedLibrary = list_of_librarys[int(
                input("Enter the the choice: "))]
