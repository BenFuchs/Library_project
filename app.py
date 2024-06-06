import sqlite3 
from enum import Enum

# Connect to SQLite database
con = sqlite3.connect('Library.db')
cur = con.cursor()

# Create books table
try:
    cur.execute("CREATE TABLE books(Name STR, Author STR, Year_published INT, Type INT, Active INT)")
except sqlite3.OperationalError:
    pass

# Create Clients table
try:
    cur.execute("CREATE TABLE Clients(Name STR, City STR, Age INT, Password, Active INT, Admin STR)")
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
    books = cur.execute(""" SELECT ROWID, * FROM books Where Active == 1""")
    print("ROWID\tName\tAuthor\tYear_published\tType")
    for book in books:
        print(f"{book[0]}\t{book[1]}\t{book[2]}\t{book[3]}\t{book[4]}")

def loan():
    pass

def return_book():
    pass

def add_book():
    if admin_check() == 1:
        b_name = input("Input book name: ")
        b_author = input("input author name: ")
        b_year = input("Input the year the book was published: ")
        b_type = int(input("Input book loan type(1/2/3): "))
        cur.execute("""    
                    INSERT INTO books VALUES
                    (?, ?, ?, ?, 1)
                    """,(b_name, b_author, b_year, b_type))
        con.commit()  
    else:
        print("This action is only accessible to Admins")
                

def remove_book():
    
    if admin_check() == 1:
        show_all_books()
        user_selection = input("please select the ID of the book you wish to delete: ")
        cur.execute("UPDATE books SET Active = 0 WHERE ROWID == ?", (user_selection))
        con.commit()
    else:
        print("This action is only accessible to Admins")

def add_client():
    c_name = input("Input Client's full name: ")
    c_city = input("input Clients city of residence: ")
    c_age = input("Input Clients age: ")
    c_password = input("Input a password for this account: ")
    cur.execute("""
                INSERT INTO Clients Values
                (?, ?, ?, ?, 1, 0)
                """, (c_name, c_city, c_age, c_password))
    con.commit()
def remove_client():
    if admin_check() == 1:
        show_all_clients()
        user_selection = input("Please select the ID of the client you wish to delete: ")
        cur.execute("UPDATE Clients SET Active = 0 WHERE ROWID = ?", (user_selection))
        con.commit()
    else:
        print("This action is only accessible to Admins")

def show_all_clients():
    clients = cur.execute(""" SELECT ROWID, * FROM Clients Where Active == 1""")
    print("ROWID\tName\tCity\tAge")
    for client in clients:
        print(f"{client[0]}\t{client[1]}\t{client[2]}\t{client[3]}")

def show_book_by_name():
    search_input = input("Please enter the name of the book you are looking for: ")
    try:
        cur.execute("SELECT * FROM books WHERE Name LIKE ? AND Active == 1", ('%' + search_input + '%',))
        books = cur.fetchall()
        if books:
            for book in books:
                print(book)
        else:
            print("Book not found")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

def show_client_by_name():
    search_input = input("Please enter the name of the client you are looking for: ")
    try:
        cur.execute("SELECT * FROM Clients WHERE Name LIKE ? AND Active == 1", ('%' + search_input + '%',))
        clients = cur.fetchall()
        if clients:
            for client in clients:
                print(client)
        else:
                print("client not found")
    except sqlite3.Error as e:
        print(f'An error occured: {e}')

def admin_check():
    user_name = input("Please enter account user name: ")
    password = input("Please enter account password: ")
    
   
    cur.execute("SELECT * FROM Clients WHERE Name = ? AND Password = ?", (user_name, password))
    pass_checks = cur.fetchall()
    
    if pass_checks:
        admin_password = "AdminPassword"  
        if password == admin_password:
            cur.execute("UPDATE Clients SET Admin = 1 WHERE Name = ? AND Password = ?", (user_name, password))
            if cur.rowcount > 0:
                print("Admin status granted.")
                return 1
            else:
                print("Failed to update admin status.")
                return 0
        else:
            print("Incorrect admin password.")
            return 0
    else:
        print("Incorrect login details.")
        return 0
        


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
