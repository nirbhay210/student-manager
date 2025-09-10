# student-manager

students = []
next_id = 1

def print_menu():
    print("\n=== Student Manager ===")
    print("1. Add Student")
    print("2. View student")
    print("3. Update student")
    print("4. Delete student")
    print("q. Quit")

def main():
    while True:
        print_menu()
        choice = input("choose an option: ").strip().lower()

        if choice == "q":
            print("Exiting Student manager. Goodbye!")
            break
        else:
            print(f"option '{choice}' not implemented yet.")


if __name__ == "__main__":
    main()