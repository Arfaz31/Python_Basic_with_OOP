
class Book:
    def __init__(self, category, id, name, quantity):
        self.id = id
        self.name = name
        self.category = category
        self.quantity = quantity

    def __repr__(self):
         #  __repr__ হচ্ছে Python-এর একটি special method (dunder method) এর full form: “representation” — মানে: কোন object কে readable string format-এ represent করা।
        return f"ID: {self.id}, Name: {self.name}, Category: {self.category}, Quantity: {self.quantity}"


class User:
    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.password = password
        self.borrowedBooks = [] # List to store borrowed books
        self.returnedBooks = []

    def __repr__(self):
        return f"ID: {self.id}, Name: {self.name}"


class Library:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.books = []  # লাইব্রেরিতে থাকা সব বই
        self.users = []  # রেজিস্টার্ড ইউজার লিস্ট

    def addBook(self, category, id, name, quantity):
        book = Book(category, id, name, quantity) # নতুন Book object তৈরি
        self.books.append(book)  # বইটি books লিস্টে যোগ
        print(f"\n'{book.name}' book added successfully!")

    def addUser(self, id, name, password):
        user = User(id, name, password)
        self.users.append(user)  # ইউজারটি users লিস্টে যোগ
        print(f"\nUser '{name}' registered successfully!")
        return user

    def borrowBook(self, user, id):
        for book in self.books:
            if book.id == id:
                if book in user.borrowedBooks:
                    print("\nBook already borrowed!")
                    return
                elif book.quantity < 1:
                    print("\nBook not available!")
                    return
                else:
                    user.borrowedBooks.append(book)
                    book.quantity -= 1
                    print(f"\n'{book.name}' borrowed successfully!")
                    return
        print("\nBook not found!")

    def returnBook(self, user, id):
        for book in user.borrowedBooks:
            if book.id == id:
                user.borrowedBooks.remove(book)
                user.returnedBooks.append(book)
                book.quantity += 1
                print(f"\n'{book.name}' returned successfully!")
                return
        print("\nBook not found in your borrowed list!")

    def showBooks(self):
        print("\nAll Books:")
        for book in self.books:
            print(f"  - {book}") # `__repr__` অনুযায়ী প্রিন্ট

    def showUsers(self):
        print("\nRegistered Users:")
        for user in self.users:
            print(f"  - {user}") # `__repr__` অনুযায়ী প্রিন্ট


# Initial setup
library = Library("My Library", "admin")
admin = library.addUser(1, "admin", "admin")
library.addUser(2, "Jane", "1234")
library.addBook("Fiction", 101, "The Great Gatsby", 5)
library.addBook("Sci-Fi", 102, "Dune", 3)

currentUser = None  # কে লগ ইন আছে, এটা ধরে রাখে
run = True  # প্রোগ্রাম চালু থাকবে কিনা

# Main loop
while run:
    if currentUser is None:
        print("\n--- Welcome to the Library ---")
        option = input("Do you want to (L)ogin or (R)egister? (L/R): ").strip().upper()
        #.strip()	ইনপুটের চারপাশের যেকোনো ফাঁকা জায়গা (space, tab, newline) সরিয়ে ফেলে দেয়ার জন্য
        if option == 'R':
            id = int(input("Enter ID: "))
            name = input("Enter Name: ")
            password = input("Enter Password: ")
            currentUser = library.addUser(id, name, password)

        elif option == 'L':
            id = int(input("Enter ID: "))
            password = input("Enter Password: ")
            for user in library.users:
                if user.id == id and user.password == password:
                    currentUser = user # Login success
                    print(f"\nLogged in as {user.name}!")
                    break
            else:
                print("\nInvalid ID or Password!")

    else:
        print(f"\n--- Hello, {currentUser.name}! ---")
        if currentUser.name == 'admin':
            print("\nOptions:")
            print("1. Add Book")
            print("2. Show All Users")
            print("3. Show All Books")
            print("4. Logout")
            print("5. Exit")

            choice = input("Enter choice: ").strip()
            if choice == '1':
                category = input("Enter Category: ")
                id = int(input("Enter Book ID: "))
                name = input("Enter Book Name: ")
                quantity = int(input("Enter Quantity: "))
                library.addBook(category, id, name, quantity)

            elif choice == '2':
                library.showUsers()

            elif choice == '3':
                library.showBooks()

            elif choice == '4':
                print(f"\nLogged out from {currentUser.name}")
                currentUser = None

            elif choice == '5':
                print("\nExiting program...")
                run = False

            else:
                print("\nInvalid option!")

        else:
            print("\nOptions:")
            print("1. Borrow Book")
            print("2. Show Borrowed Books")
            print("3. Show All Books")
            print("4. Return Book")
            print("5. Show Returned Books")
            print("6. Logout")
            print("7. Exit")

            choice = input("Enter choice: ").strip()
            if choice == '1':
                id = int(input("Enter Book ID to borrow: "))
                library.borrowBook(currentUser, id)

            elif choice == '2':
                print("\nYour Borrowed Books:")
                for book in currentUser.borrowedBooks:
                    print(f"  - {book}")

            elif choice == '3':
                library.showBooks()

            elif choice == '4':
                id = int(input("Enter Book ID to return: "))
                library.returnBook(currentUser, id)

            elif choice == '5':
                print("\nYour Returned Books:")
                for book in currentUser.returnedBooks:
                    print(f"  - {book}") # book `__repr__` অনুযায়ী প্রিন্ট

            elif choice == '6':
                print(f"\nLogged out from {currentUser.name}")
                currentUser = None

            elif choice == '7':
                print("\nExiting program...")
                run = False

            else:
                print("\nInvalid option!")

