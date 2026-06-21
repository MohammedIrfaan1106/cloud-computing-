
from auth import register_user, login_user
from storage import upload_file, list_files, delete_file, search_file, storage_usage
from database import initialize_database

initialize_database()

while True:
    print("\n=== CLOUD STORAGE EXPLORER ===")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        register_user()
    elif choice == "2":
        user = login_user()
        if user:
            while True:
                print(f"\nWelcome {user}")
                print("1. Upload File")
                print("2. List Files")
                print("3. Delete File")
                print("4. Search File")
                print("5. Storage Usage")
                print("6. Logout")

                c = input("Enter choice: ")

                if c == "1":
                    upload_file(user)
                elif c == "2":
                    list_files(user)
                elif c == "3":
                    delete_file(user)
                elif c == "4":
                    search_file(user)
                elif c == "5":
                    storage_usage(user)
                elif c == "6":
                    break
    elif choice == "3":
        break
