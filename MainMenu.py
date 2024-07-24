def main_menu():
    with connect_to_db('library.db') as conn:
        print("Welcome to the Library Management System!")
        print("Main Menu:")
        print("1. Book Operations")
        print("2. Genre Operations")
        print("3. User Operations")
        print("4. Author Operations")
        print("5. Quit")

        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("Enter the book title: ")
            author = input("Enter the book author: ")
            isbn = input("Enter the book ISBN: ")
            if not validate_isbn(isbn):
                print("Invalid ISBN format.")
                return
            publication_date = input("Enter the publication date: ")
            add_book(conn, title, author, isbn, publication_date)
        elif choice == "2":
            name = input("Enter the genre name: ")
            add_genre(conn, name)
        elif choice == "3":
            user_id = input("Enter the user ID: ")
            name = input("Enter the user name: ")
            email = input("Enter the user email: ")
            add_user(conn, user_id, name, email)
        elif choice == "4":
            name = input("Enter the author name: ")
            add_author(conn, name)
        elif choice == "5":
            print("Thank you for using the Library Management System.")
            exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
