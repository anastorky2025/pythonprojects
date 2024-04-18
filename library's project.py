import os

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

book_catalog = {}
availability = {}

while True:
    clear_screen()
    user_choice = input("""
Menu:
1- Add Book
2- Check Out Book
3- Check In Book
4- List Books
5- Exit
Enter your choice (1-5): 
""")
    if user_choice == "5":
        break
    
    elif user_choice == "1":
        while True:
            while True:
                isbn = int(input("Enter ISBN: "))
                if isbn in book_catalog:
                    print("That ISBN is already in the catalog.")
                else:
                    break

            title = input("Enter title: ")
            author = input("Enter author: ")
            book_catalog[isbn] = [title, author]
            availability[isbn] = True
            print(f"Book '{title}' by {author} added to the catalog with ISBN {isbn}. ")
            add_another_book = input("Do you want to add another book? (y/n): ")
            if add_another_book == "n":
                break
            clear_screen()
    
    elif user_choice == "2":
        while True:
            to_check_out = int(input("Enter ISBN to check out: "))
            if availability[to_check_out]:
                availability[to_check_out] = False
                book_name = book_catalog[to_check_out][0]
                print(f"Book '{book_name}' checked out successfully.")
            else:
                print("Book not found or already checked out.")
            check_out_another_book = input("Do you want to check out another book? (y/n): ")
            if check_out_another_book == "n":
                break
    
    elif user_choice == "3":
        while True:
            to_check_in = int(input("Enter ISBN to check in: "))
            if to_check_in not in book_catalog:
                print("Book not found in the catalog.")
            else:
                availability[to_check_in] = True
                print(f"Book '{book_catalog[to_check_in][0]}' checked in successfully.")
            check_in_another_book = input("Do you want to check in another book? (y/n): ")
            if check_in_another_book == "n":
                break
    
    elif user_choice == "4":
        for isbn, details in book_catalog.items():
            availability_status = "Available" if availability[isbn] else "Not Available"
            print(f"ISBN: {isbn}, Title: {details[0]}, Author: {details[1]}, Availability: {availability_status}")
        input("Press Enter to continue...")
