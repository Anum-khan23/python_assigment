import json
import streamlit as st

# Load and save library data
def load_library():
    try:
        with open('library.txt', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_library():
    with open('library.txt', 'w') as file:
        json.dump(library, file, indent=4)

# Initialize library
library = load_library()

def add_book():
    st.subheader("Add a New Book")
    title = st.text_input("Book Title")
    author = st.text_input("Author")
    year = st.number_input("Year", min_value=1000, max_value=9999, step=1)
    read = st.checkbox("Read")

    if st.button("Add Book"):
        if title and author:
            new_book = {'title': title, 'author': author, 'year': year, 'read': read}
            library.append(new_book)
            save_library()
            st.success(f"Added: {title}")
        else:
            st.error("Please enter both Title and Author.")

    # Display book list after adding
    display_books()

def remove_book():
    st.subheader("Remove a Book")
    title = st.text_input("Title to remove")

    if st.button("Remove"):
        global library
        updated_library = [book for book in library if book.get('title', '').lower() != title.lower()]
        
        if len(updated_library) == len(library):
            st.warning(f"No book found with title: {title}")
        else:
            library = updated_library
            save_library()
            st.success(f"Removed: {title}")

    # Display book list after removing
    display_books()

def display_books():
    """Function to display all books"""
    st.subheader("📚 Book List")
    if not library:
        st.write("No books in the library.")
    else:
        for book in library:
            title = book.get("title", "Unknown Title")
            author = book.get("author", "Unknown Author")
            year = book.get("year", "Unknown Year")
            read_status = "✅ Read" if book.get("read", False) else "❌ Not Read"

            st.write(f"📖 **Title:** {title} | ✍ **Author:** {author} | 📅 **Year:** {year} | {read_status}")

def main():
    st.title("📖 Book Manager")
    choice = st.selectbox("Menu", ["Add Book", "Remove Book"])
    {'Add Book': add_book, 'Remove Book': remove_book}[choice]()

if __name__ == "__main__":
    main()






















# import json
# import streamlit as st

# # Initialize the library list
# library = []

# # Load the library from a file (if exists)
# def load_library():
#     global library
#     try:
#         with open('library.txt', 'r') as file:
#             library = json.load(file)
#         st.success("Library loaded from file.")
#     except FileNotFoundError:
#         st.info("No previous library data found. Starting fresh!")

# # Save the library to a file
# def save_library():
#     with open('library.txt', 'w') as file:
#         json.dump(library, file)
#     st.success("Library saved to file.")

# # Function to add a book to the library
# def add_book():
#     title = st.text_input("Enter the book title:")
#     author = st.text_input("Enter the author:")
#     year = st.number_input("Enter the publication year:", min_value=1000, max_value=9999, step=1)
#     genre = st.text_input("Enter the genre:")
#     read_status = st.radio("Have you read this book?", ("Yes", "No"))

#     if st.button("Add Book"):
#         book = {
#             'title': title,
#             'author': author,
#             'year': year,
#             'genre': genre,
#             'read': read_status == 'Yes'
#         }
#         library.append(book)
#         st.success(f"Book '{title}' added successfully!")

# # Function to remove a book from the library
# def remove_book():
#     title = st.text_input("Enter the title of the book to remove:")
#     if st.button("Remove Book"):
#         for book in library:
#             if book['title'].lower() == title.lower():
#                 library.remove(book)
#                 st.success(f"Book '{title}' removed successfully!")
#                 return
#         st.error(f"No book found with title '{title}'.")

# # Function to search for a book by title or author
# def search_book():
#     st.subheader("Search for a Book")
#     choice = st.radio("Search by:", ("Title", "Author"))
#     if choice == "Title":
#         title = st.text_input("Enter the title:")
#         matching_books = [book for book in library if title.lower() in book['title'].lower()]
#     else:
#         author = st.text_input("Enter the author:")
#         matching_books = [book for book in library if author.lower() in book['author'].lower()]

#     if matching_books:
#         st.write("Matching Books:")
#         for book in matching_books:
#             read_status = "Read" if book['read'] else "Unread"
#             st.write(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
#     else:
#         st.info("No matching books found.")

# # Function to display all books
# def display_books():
#     if library:
#         st.subheader("Your Library:")
#         for idx, book in enumerate(library, 1):
#             read_status = "Read" if book['read'] else "Unread"
#             st.write(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
#     else:
#         st.info("Your library is empty!")

# # Function to display statistics
# def display_statistics():
#     total_books = len(library)
#     if total_books == 0:
#         st.info("No books in the library.")
#     else:
#         read_books = sum(1 for book in library if book['read'])
#         percentage_read = (read_books / total_books) * 100
#         st.write(f"Total books: {total_books}")
#         st.write(f"Percentage read: {percentage_read:.2f}%")

# # Main function to show the menu and process user input
# def main():
#     st.title("Personal Library Manager")
#     load_library()

#     menu = ["Add a Book", "Remove a Book", "Search for a Book", "Display All Books", "Display Statistics", "Exit"]
#     choice = st.selectbox("Choose an option:", menu)

#     if choice == "Add a Book":
#         add_book()
#     elif choice == "Remove a Book":
#         remove_book()
#     elif choice == "Search for a Book":
#         search_book()
#     elif choice == "Display All Books":
#         display_books()
#     elif choice == "Display Statistics":
#         display_statistics()
#     elif choice == "Exit":
#         save_library()
#         st.balloons()
#         st.success("Library saved to file. Goodbye!")

# if __name__ == "__main__":
#     main()
