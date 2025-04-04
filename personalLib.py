import json

# Initialize the library list
library = []

# Load the library from a file (if exists)
def load_library():
    global library
    try:
        with open('library.txt', 'r') as file:
            library = json.load(file)
        print("Library loaded from file.")
    except FileNotFoundError:
        print("No previous library data found. Starting fresh!")

# Save the library to a file
def save_library():
    with open('library.txt', 'w') as file:
        json.dump(library, file)
    print("Library saved to file.")

# Function to add a book to the library
def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read_status = input("Have you read this book? (yes/no): ").lower() == 'yes'
    
    book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read': read_status
    }
    
    library.append(book)
    print(f"Book '{title}' added successfully!")

# Function to remove a book from the library
def remove_book():
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book['title'].lower() == title.lower():
            library.remove(book)
            print(f"Book '{title}' removed successfully!")
            return
    print(f"No book found with title '{title}'.")

# Function to search for a book by title or author
def search_book():
    print("Search by:")
    print("1. Title")
    print("2. Author")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        title = input("Enter the title: ")
        matching_books = [book for book in library if title.lower() in book['title'].lower()]
    elif choice == '2':
        author = input("Enter the author: ")
        matching_books = [book for book in library if author.lower() in book['author'].lower()]
    else:
        print("Invalid choice.")
        return
    
    if matching_books:
        print("Matching Books:")
        for idx, book in enumerate(matching_books, 1):
            read_status = "Read" if book['read'] else "Unread"
            print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
    else:
        print("No matching books found.")

# Function to display all books
def display_books():
    if library:
        print("Your Library:")
        for idx, book in enumerate(library, 1):
            read_status = "Read" if book['read'] else "Unread"
            print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
    else:
        print("Your library is empty!")

# Function to display statistics
def display_statistics():
    total_books = len(library)
    if total_books == 0:
        print("No books in the library.")
    else:
        read_books = sum(1 for book in library if book['read'])
        percentage_read = (read_books / total_books) * 100
        print(f"Total books: {total_books}")
        print(f"Percentage read: {percentage_read:.2f}%")

# Main function to show the menu and process user input
def main():
    load_library()
    
    while True:
        print("\nWelcome to your Personal Library Manager!")
        print("Menu")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_book()
        elif choice == '2':
            remove_book()
        elif choice == '3':
            search_book()
        elif choice == '4':
            display_books()
        elif choice == '5':
            display_statistics()
        elif choice == '6':
            save_library()
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
