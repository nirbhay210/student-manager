# student-manager

students = []
next_id = 1



def _read_int(prompt):
    while True:
        raw = input(prompt).strip()
        if raw.isdigit():
            return int(raw)
        print("invalid number. Please entera valid integer.")

def add_student():
    global next_id
    name = input("Name: ").strip()
    age = _read_int("Age: ")
    grade = input("Grade (e.g. , A/B/C): ").strip().upper()

    record = {"id": next_id, "name": name, "age": age, "grade": grade}
    students.append(record)
    print(f"Added student #{next_id}: {name}")
    next_id +=1

def print_menu():
    print("\n=== Student Manager ===")
    print("1. Add Student")
    print("2. View student")
    print("3. Update student")
    print("4. Delete student")
    print("q. Quit")

def handle_choice(choice):
    if choice == "1":
        add_student()
    else:
        print(f"option '{choice}' not implemented yet")

def main():
    while True:
        print_menu()
        choice = input("choose an option: ").strip().lower()

        if choice == "q":
            print("Exiting Student manager. Goodbye!")
            break
        handle_choice(choice)
#        else:
#            print(f"option '{choice}' not implemented yet.")


if __name__ == "__main__":
    main()



