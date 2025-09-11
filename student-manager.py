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

def view_students():
    if not students:
        print("No students yet.")
        return
    print("\nID. | Name                 |  Age  |  Grade")
    print("-----------------------------------------------")
    for s in students:
        print(f"{s['id']:<3} | {s['name']:<20} | {s['age']:<3} | {s['grade']}")

def find_index_by_id(target_id: int) -> int:
    """Return list index for student with id==target_id, else -1."""
    for i, s in enumerate(students):
        if s["id"] == target_id:
            return i
    return -1


def update_student():
    """Edit fields; press Enter to keep existing value."""
    # ask which ID to edit
    raw = input("Enter ID to update: ").strip()
    if not raw.isdigit():
        print("Invalid ID.")
        return
    target_id = int(raw)

    idx = find_index_by_id(target_id)
    if idx == -1:
        print("ID not found.")
        return

    current = students[idx]
    print(f"Editing #{current['id']} (press Enter to keep current value)")


    new_name = input(f"Name [{current['name']}]: ").strip()
    if new_name:
        current["name"] = new_name


    raw_age = input(f"Age [{current['age']}]: ").strip()
    if raw_age:
        if raw_age.isdigit():
            current["age"] = int(raw_age)
        else:
            print("Invalid age; keeping old value.")

    # Grade
    new_grade = input(f"Grade [{current['grade']}]: ").strip()
    if new_grade:
        current["grade"] = new_grade.upper()

    print("Updated.")


def delete_student():

    raw = input("Enter ID to delete: ").strip()
    if not raw.isdigit():
        print("Invalid ID.")
        return
    target_id = int(raw)

    idx = find_index_by_id(target_id)  # uses the finder you added earlier
    if idx == -1:
        print("ID not found.")
        return

    removed = students.pop(idx)  # remove by index
    print(f"Deleted #{removed['id']} ({removed['name']}).")

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
    elif choice =="2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    else:
        print("Invalid choice")

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



