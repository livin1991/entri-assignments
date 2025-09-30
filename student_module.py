# student_module.py
import datetime
import csv

def generate_id(existing_ids):
    """Auto-generate a unique student ID"""
    if not existing_ids:
        return 1
    else:
        return max(existing_ids) + 1

def get_timestamp():
    """Return current date and time as string"""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def validate_integer(input_str, field_name):
    """Validate that input is an integer"""
    try:
        value = int(input_str)
        return value
    except ValueError:
        print(f"❌ Invalid {field_name}. Please enter a number.")
        return None

def load_students(filename="students.txt"):
    """Load students from file"""
    students = []
    try:
        with open(filename, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["ID"] = int(row["ID"])
                row["Age"] = int(row["Age"])
                row["Marks"] = float(row["Marks"])
                students.append(row)
    except FileNotFoundError:
        pass
    return students

def save_students(students, filename="students.txt"):
    """Save students to file"""
    with open(filename, "w", newline="") as file:
        fieldnames = ["ID", "Name", "Roll", "Age", "Department", "Marks", "Timestamp"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)
