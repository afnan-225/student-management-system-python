library = {}

def show_menu():
    print("\n--- LIBRARY MANAGEMENT SYSTEM ---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    library[book_id] = {
        "Title": title,
        "Author": author,
        "Issued": False
    }
    print("Book added successfully!")

def view_books():
    if not library:
        print("No books available.")
    else:
        print("\nLibrary Books:")
        for book_id, details in library.items():
            status = "Issued" if details["Issued"] else "Available"
            print(f"ID: {book_id}, Title: {details['Title']}, Status: {status}")

def search_book():
    book_id = input("Enter Book ID to search: ")
    if book_id in library:
        details = library[book_id]
        print(f"Title: {details['Title']}")
        print(f"Author: {details['Author']}")
        print(f"Status: {'Issued' if details['Issued'] else 'Available'}")
    else:
        print("Book not found.")

def issue_book():
    book_id = input("Enter Book ID to issue: ")
    if book_id in library and not library[book_id]["Issued"]:
        library[book_id]["Issued"] = True
        print("Book issued successfully.")
    else:
        print("Book not available.")

def return_book():
    book_id = input("Enter Book ID to return: ")
    if book_id in library and library[book_id]["Issued"]:
        library[book_id]["Issued"] = False
        print("Book returned successfully.")
    else:
        print("Invalid return request.")

while True:
    show_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_book()
    elif choice == '2':
        view_books()
    elif choice == '3':
        search_book()
    elif choice == '4':
        issue_book()
    elif choice == '5':
        return_book()
    elif choice == '6':
        print("Exiting system.")
        break
    else:
        print("Invalid choice.")
