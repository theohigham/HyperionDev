import sqlite3

# Define the database connection and cursor
conn = sqlite3.connect('ebookstore.db')
c = conn.cursor()

# Create the books table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS books
             (id INTEGER PRIMARY KEY,
              title TEXT,
              author TEXT,
              qty INTEGER)''')

# Insert some initial data into the books table
c.execute("INSERT INTO books (id, title, author, qty) VALUES (3001, 'A Tale of Two Cities', 'Charles Dickens', 30)")
c.execute("INSERT INTO books (id, title, author, qty) VALUES (3002, 'Harry Potter and the Philosopher''s Stone', 'J.K. Rowling', 40)")
c.execute("INSERT INTO books (id, title, author, qty) VALUES (3003, 'The Lion, the Witch and the Wardrobe', 'C. S. Lewis', 25)")
c.execute("INSERT INTO books (id, title, author, qty) VALUES (3004, 'The Lord of the Rings', 'J.R.R Tolkien', 37)")
c.execute("INSERT INTO books (id, title, author, qty) VALUES (3005, 'Alice in Wonderland', 'Lewis Carroll', 12)")

# Define functions for each option in the menu
def add_book():
    id = input("Enter book ID: ")
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    qty = input("Enter quantity: ")
    c.execute("INSERT INTO books (id, title, author, qty) VALUES (?, ?, ?, ?)", (id, title, author, qty))
    conn.commit()
    print("Book added to the database.")

def update_book():
    id = input("Enter book ID to update: ")
    title = input("Enter new book title (leave blank if not updating): ")
    author = input("Enter new book author (leave blank if not updating): ")
    qty = input("Enter new quantity (leave blank if not updating): ")
    if title:
        c.execute("UPDATE books SET title=? WHERE id=?", (title, id))
    if author:
        c.execute("UPDATE books SET author=? WHERE id=?", (author, id))
    if qty:
        c.execute("UPDATE books SET qty=? WHERE id=?", (qty, id))
    conn.commit()
    print("Book updated.")

def delete_book():
    id = input("Enter book ID to delete: ")
    c.execute("DELETE FROM books WHERE id=?", (id,))
    conn.commit()
    print("Book deleted from the database.")

def search_book():
    term = input("Enter search term: ")
    c.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ?", ('%' + term + '%', '%' + term + '%'))
    results = c.fetchall()
    if len(results) == 0:
        print("No books found.")
    else:
        for result in results:
            print("ID:", result[0])
            print("Title:", result[1])
            print("Author:", result[2])
            print("Quantity:", result[3])
            print()

# Display the menu and ask the user for input
while True:
    print("1. Enter book")
    print("2. Update book")
    print("3. Delete book")
    print("4. Search books")
    print("0. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        add_book()
    elif choice == '2':
        update_book()
    elif choice == '3':
        delete_book()
    elif choice == '4':
        search_book()
    elif choice == '0':
        print("Goodbye!")
        break

