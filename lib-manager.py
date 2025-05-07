import json 
import os

data_file = "lib.txt"

def load_lib():
    if os.path.exists(data_file):
        with open(data_file, "r") as file:
            return json.load(file)
    return []


def save_lib(library):
    with open(data_file, "w") as file:
        json.dump(library, file)


def add_book(library):
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    year = input("Enter book year: ")
    genre = input("Enter book genre: ")
    read = input("Have you read this book? (yes/no): ").lower() == "yes"

    new_book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }

    library.append(new_book)
    save_lib(library)
    print(f"Book '{title}' added to the library.")


def remove_book(library):
    title = input("Enter the title of the book to remove: ")
    initial_length = len(library)
    library = [book for book in library if book["title"].lower() != title.lower()]
    if len(library) < initial_length:
        save_lib(library)
        print(f"Book '{title}' removed from the library.")
    else:
        print(f"Book '{title}' not found in the library.")

def search_books(library):
    search_by = input("Search by (title/author): ").lower()
    search_term = input(f"Enter the {search_by} ").lower()
    results = [book for book in library if search_term in book[search_by].lower()]

    if results:
        for book in results:
            status = "Read" if book["read"] else "Not Read" 
            print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}, Read: {'Yes' if book['read'] else 'No'}")
    else:
        print(f"No books found matching {search_term} in the {search_by} field.")

def display_all_books(library):
    if library:
        for book in library:
            status = "Read" if book["read"] else "Not Read" 
            print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}, Read: {'Yes' if book['read'] else 'No'}")
    else:
        print("No books in the library.")

def display_stats(library):
    total_books = len(library)
    read_books = len([book for book in library if book["read"]])
    percentage_read = (read_books / total_books * 100) if total_books > 0 else 0
    unread_books = total_books - read_books


    print(f"Total books: {total_books}")
    print(f"Books read: {read_books}")
    print(f"percentage read: {percentage_read:.2f}%")
    print(f"Books not read: {unread_books}")

def main():
    library = load_lib()

    while True:
        print("\nLibrary Management System")
        print("Menu")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Books")
        print("4. Display All Books")
        print("5. Display Statistics")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_books(library)
        elif choice == "4":
            display_all_books(library)
        elif choice == "5":
            display_stats(library)
        elif choice == "6":
            print("Exiting the library.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
# This code is a simple library management system that allows users to add, remove, search, and display books in a library.