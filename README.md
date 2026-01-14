# student-management-system-python
# A menu-driven Student Management System built using Python with file handling.
students = {}
FILE_NAME = "students.txt"

def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                roll, name, marks = line.strip().split(",")
                students[roll] = {"Name": name, "Marks": marks}
    except FileNotFoundError:
        pass

def save_data():
    with open(FILE_NAME, "w") as file:
        for roll, details in students.items():
            file.write(f"{roll},{details['Name']},{details['Marks']}\n")

def show_menu():
    print("\n--- STUDENT MANAGEMENT SYSTEM ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    marks = input("Enter Marks: ")
    students[roll] = {"Name": name, "Marks": marks}
    save_data()
    print("Student added successfully!")

def view_students():
    if not students:
        print("No student records found.")
    else:
        print("\nStudent Records:")
        for roll, details in students.items():
            print(f"Roll: {roll}, Name: {details['Name']}, Marks: {details['Marks']}")

def search_student():
    roll = input("Enter Roll Number to search: ")
    if roll in students:
        print(f"Name: {students[roll]['Name']}")
        print(f"Marks: {students[roll]['Marks']}")
    else:
        print("Student not found.")

def update_student():
    roll = input("Enter Roll Number to update: ")
    if roll in students:
        name = input("Enter new name: ")
        marks = input("Enter new marks: ")
        students[roll]["Name"] = name
        students[roll]["Marks"] = marks
        save_data()
        print("Student record updated successfully.")
    else:
        print("Student not found.")

def delete_student():
    roll = input("Enter Roll Number to delete: ")
    if roll in students:
        del students[roll]
        save_data()
        print("Student deleted successfully.")
    else:
        print("Student not found.")

load_data()

while True:
    show_menu()
    choice = input("Enter your choice (1-6): ")
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Try again.")
