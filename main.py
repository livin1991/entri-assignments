import getpass
import sys
from student_module import generate_id, get_timestamp, validate_integer, load_students, save_students

CREDENTIALS = {
    "admin": "admin123",
    "teacher": "teacher123"
}

students = load_students()

# ------------------- LOGIN -------------------
def login():
    print("===== Student Management System Login =====")
    for attempt in range(3):
        username = input("Enter username: ").strip()
        try:
            password = getpass.getpass("Enter password: ")
        except:
            password = input("Enter password: ")

        if username in CREDENTIALS and CREDENTIALS[username] == password:
            print(f"✅ Login successful! Welcome, {username}.")
            return True
        else:
            print("❌ Invalid username or password. Try again.")
    print("🚫 Too many failed attempts. Exiting...")
    sys.exit(0)

# ------------------- ADD STUDENT -------------------
def add_student():
    print("\n--- Add New Student ---")
    name = input("Name: ").strip()
    roll = input("Roll Number: ").strip()

    age = None
    while age is None:
        age = validate_integer(input("Age: "), "Age")

    dept = input("Department: ").strip()

    marks = None
    while marks is None:
        try:
            marks = float(input("Marks: "))
        except ValueError:
            print("❌ Invalid Marks. Please enter a number.")

    existing_ids = [s["ID"] for s in students]
    student_id = generate_id(existing_ids)
    timestamp = get_timestamp()

    student = {
        "ID": student_id,
        "Name": name,
        "Roll": roll,
        "Age": age,
        "Department": dept,
        "Marks": marks,
        "Timestamp": timestamp
    }
    students.append(student)
    save_students(students)
    print(f"✅ Student {name} added successfully with ID {student_id} at {timestamp}.\n")

# ------------------- VIEW STUDENTS -------------------
def view_students():
    print("\n--- Student Records ---")
    if not students:
        print("No records found.\n")
        return
    for s in students:
        print(f"ID:{s['ID']}, Name:{s['Name']}, Roll:{s['Roll']}, Age:{s['Age']}, Dept:{s['Department']}, Marks:{s['Marks']}, Added:{s['Timestamp']}")
    print()

# ------------------- UPDATE STUDENT -------------------
def update_student():
    print("\n--- Update Student Record ---")
    try:
        student_id = int(input("Enter Student ID to update: "))
    except ValueError:
        print("❌ Invalid ID.")
        return

    for s in students:
        if s["ID"] == student_id:
            print(f"Current Info: {s}")
            name = input("New Name (press Enter to keep current): ").strip() or s["Name"]
            roll = input("New Roll (press Enter to keep current): ").strip() or s["Roll"]

            age = None
            while age is None:
                temp = input(f"New Age (current {s['Age']}): ").strip()
                age = s["Age"] if temp == "" else validate_integer(temp, "Age")

            dept = input(f"New Department (current {s['Department']}): ").strip() or s["Department"]

            marks = None
            while marks is None:
                temp = input(f"New Marks (current {s['Marks']}): ").strip()
                if temp == "":
                    marks = s["Marks"]
                else:
                    try:
                        marks = float(temp)
                    except ValueError:
                        print("❌ Invalid Marks. Please enter a number.")

            s.update({"Name": name, "Roll": roll, "Age": age, "Department": dept, "Marks": marks})
            save_students(students)
            print("✅ Student record updated successfully.\n")
            return

    print("❌ Student ID not found.\n")

# ------------------- DELETE STUDENT -------------------
def delete_student():
    print("\n--- Delete Student Record ---")
    try:
        student_id = int(input("Enter Student ID to delete: "))
    except ValueError:
        print("❌ Invalid ID.")
        return

    for s in students:
        if s["ID"] == student_id:
            students.remove(s)
            save_students(students)
            print(f"✅ Student record deleted successfully.\n")
            return

    print("❌ Student ID not found.\n")

# ------------------- SEARCH STUDENT -------------------
def search_student():
    print("\n--- Search Student ---")
    keyword = input("Enter Name or Department to search: ").strip().lower()
    results = [s for s in students if keyword in s["Name"].lower() or keyword in s["Department"].lower()]
    if not results:
        print("❌ No matching records found.\n")
        return
    for s in results:
        print(f"ID:{s['ID']}, Name:{s['Name']}, Roll:{s['Roll']}, Dept:{s['Department']}, Marks:{s['Marks']}")
    print()

# ------------------- TOP STUDENTS -------------------
def top_students():
    print("\n--- Top Performing Students ---")
    if not students:
        print("No records found.\n")
        return
    sorted_students = sorted(students, key=lambda x: x["Marks"], reverse=True)
    top = sorted_students[:5]  # Top 5 students
    for s in top:
        print(f"ID:{s['ID']}, Name:{s['Name']}, Marks:{s['Marks']}")
    print()

# ------------------- MAIN MENU -------------------
def main_menu():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. Top Students")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            search_student()
        elif choice == "6":
            top_students()
        elif choice == "7":
            print("✅ Exiting system. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

# ------------------- RUN PROGRAM -------------------
if __name__ == "__main__":
    if login():
        main_menu()
