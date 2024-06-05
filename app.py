import sqlite3 
from enum import Enum

# Connect to SQLite database
con = sqlite3.connect('Library.db')
cur = con.cursor()

# Create books table
try:
    cur.execute("CREATE TABLE books(Name STR, Author STR, Year_published INT, Type INT)")
except sqlite3.OperationalError:
    pass

# Create Clients table
try:
    cur.execute("CREATE TABLE Clients(Name STR, City STR, Age INT)")
except sqlite3.OperationalError:
    pass

# Create Loans table
try:
    cur.execute("CREATE TABLE Loans(Book_ID INT, Client_ID INT, Loan_date STR, Return_date STR)")
except sqlite3.OperationalError:
    pass

# Enum for actions
class actions(Enum):
    SHOW_ALL_BOOKS = 1
    LOAN_BOOK = 2
    RETURN_BOOK = 3
    ADD_BOOK = 4
    REMOVE_BOOK = 5
    ADD_CLIENT = 6
    REMOVE_CLIENT = 7
    SHOW_ALL_CLIENTS = 8
    SHOW_BOOK_BY_NAME = 9
    SHOW_CLIENT_BY_NAME = 10
    EXIT = 11


def menu():
    for action in actions:
        print(f'{action.name} - {action.value}')
    return int(input("Please input selected action: "))

def show_all_books():
    books = cur.execute(""" SELECT ROWID, * FROM books """)
    print("ROWID\tName\tAuthor\tYear_published\tType")
    for book in books:
        print(f"{book[0]}\t{book[1]}\t{book[2]}\t{book[3]}\t{book[4]}")

def loan():
    pass

def return_book():
    pass

def add_book():
    b_name = input("Input book name: ")
    b_author = input("input author name: ")
    b_year = input("Input the year the book was published: ")
    b_type = int(input("Input book loan type(1/2/3): "))
    cur.execute("""    
                INSERT INTO books VALUES
                (?, ?, ?, ?)
                 """,(b_name, b_author, b_year, b_type))
    con.commit()  
                

def remove_book():
    show_all_books()
    user_selection = input("please select the ID of the book you wish to delete: ")
    cur.execute(" DELETE from books where ROWID = ?", (user_selection))
    con.commit()

def add_client():
    pass

def remove_client():
    pass

def show_all_clients():
    pass

def show_book_by_name():
    search_input = input("Please enter the name of the book you wish to see: ")
    try:
        cur.execute("SELECT * FROM books WHERE Name LIKE ?", ('%' + search_input + '%',))
        books = cur.fetchall()
        if books:
            for book in books:
                print(book)
        else:
            print("Book not found")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

def show_client_by_name():
    pass

# Main loop
if __name__ == '__main__':
    while True:
        user_input = menu()
        if user_input == actions.SHOW_ALL_BOOKS.value: show_all_books()
        if user_input == actions.LOAN_BOOK.value: loan()
        if user_input == actions.RETURN_BOOK.value: return_book()
        if user_input == actions.ADD_BOOK.value: add_book()
        if user_input == actions.REMOVE_BOOK.value: remove_book()
        if user_input == actions.ADD_CLIENT.value: add_client()
        if user_input == actions.REMOVE_CLIENT.value: remove_client()
        if user_input == actions.SHOW_ALL_CLIENTS.value: show_all_clients()
        if user_input == actions.SHOW_BOOK_BY_NAME.value: show_book_by_name()
        if user_input == actions.SHOW_CLIENT_BY_NAME.value: show_client_by_name()
        if user_input == actions.EXIT.value:
            print("Exiting the program.")
            break


con.commit()
con.close()