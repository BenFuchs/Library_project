# Project - Library
   This project sets to emulate a functioning library with dB's for the books, clients and loans.

## type explanation
   The book type set the maximum loan time for the book: 
    • 1 – up to 10 days 
    • 2 – up to 5 days 
    • 3 – up to 2 days
## Active explanation 
   The Active coloumn in both books and clients table represents if the row is active or not. an inactive book will not show in the show_all_books function
   and an inactive client will not be able to loan out new books.

## Admin explanation
   The Admin coloumn is set up in such a way that only a Admin will have the value be set to 1. Admins will have access to functions that normal clients will not have, such as:
   `add_book()`
   `remove_book()`
   `remove_client()`

## Function List and Progress Tracking

1. `show_all_books()`
   - **Status:** Done

2. `loan()`
   - **Status:** WIP (Return date needs to be tweaked, more minor adjustments and cleanup required)

3. `return_book()`
   - **Status:** Not started (pass statement)

4. `add_book()`
   - **Status:** Done

5. `remove_book()`
   - **Status:** Done

6. `add_client()`
   - **Status:** Done
7. `remove_client()`
   - **Status:** Done

8. `show_all_clients()`
   - **Status:** Done

9. `show_book_by_name()`
   - **Status:** Done

10. `show_client_by_name()`
    - **Status:** Done

11. `admin_check()`
    - **Status:** Done