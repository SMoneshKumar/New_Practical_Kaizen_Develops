import json
import os

FILE_NAME = "students.json"


# ---------------------------------------------------------
# LOAD STUDENTS
# ---------------------------------------------------------

def load_students():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except:
            return []
    return []


# ---------------------------------------------------------
# SAVE STUDENTS
# ---------------------------------------------------------

def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


# ---------------------------------------------------------
# GENERATE STUDENT ID
# ---------------------------------------------------------

def generate_student_id(students):
    if not students:
        return 1

    ids = [student["id"] for student in students]
    return max(ids) + 1


# ---------------------------------------------------------
# CALCULATE AVERAGE
# ---------------------------------------------------------

def calculate_average(marks):
    if not marks:
        return 0

    return sum(marks.values()) / len(marks)


# ---------------------------------------------------------
# CALCULATE GRADE
# ---------------------------------------------------------

def calculate_grade(average):

    if average >= 90:
        return "A+"

    elif average >= 80:
        return "A"

    elif average >= 70:
        return "B"

    elif average >= 60:
        return "C"

    elif average >= 50:
        return "D"

    else:
        return "F"


# ---------------------------------------------------------
# ADD STUDENT
# ---------------------------------------------------------

def add_student(students):

    print("\n========== ADD STUDENT ==========")

    name = input("Enter student name: ").strip()

    if name == "":
        print("Name cannot be empty.")
        return

    age = input("Enter age: ").strip()

    if not age.isdigit():
        print("Invalid age.")
        return

    age = int(age)

    course = input("Enter course: ").strip()

    if course == "":
        print("Course cannot be empty.")
        return

    print("\nEnter marks:")

    subjects = ["Python", "Data Structures", "Database", "Mathematics"]

    marks = {}

    for subject in subjects:

        while True:

            value = input(f"{subject}: ")

            try:
                mark = float(value)

                if 0 <= mark <= 100:
                    marks[subject] = mark
                    break

                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    average = calculate_average(marks)
    grade = calculate_grade(average)

    student = {
        "id": generate_student_id(students),
        "name": name,
        "age": age,
        "course": course,
        "marks": marks,
        "average": round(average, 2),
        "grade": grade
    }

    students.append(student)

    save_students(students)

    print("\nStudent added successfully!")
    print("Student ID:", student["id"])


# ---------------------------------------------------------
# DISPLAY ONE STUDENT
# ---------------------------------------------------------

def display_student(student):

    print("\n----------------------------------")
    print("Student ID :", student["id"])
    print("Name       :", student["name"])
    print("Age        :", student["age"])
    print("Course     :", student["course"])

    print("\nMarks:")

    for subject, mark in student["marks"].items():
        print(f"{subject:<20}: {mark}")

    print("\nAverage    :", student["average"])
    print("Grade      :", student["grade"])
    print("----------------------------------")


# ---------------------------------------------------------
# VIEW ALL STUDENTS
# ---------------------------------------------------------

def view_students(students):

    print("\n========== ALL STUDENTS ==========")

    if not students:
        print("No students found.")
        return

    for student in students:
        display_student(student)


# ---------------------------------------------------------
# SEARCH STUDENT
# ---------------------------------------------------------

def search_student(students):

    print("\n========== SEARCH STUDENT ==========")

    if not students:
        print("No students available.")
        return

    print("1. Search by ID")
    print("2. Search by Name")

    choice = input("Enter choice: ")

    if choice == "1":

        value = input("Enter student ID: ")

        if not value.isdigit():
            print("Invalid ID.")
            return

        student_id = int(value)

        for student in students:

            if student["id"] == student_id:
                display_student(student)
                return

        print("Student not found.")

    elif choice == "2":

        name = input("Enter student name: ").lower()

        found = False

        for student in students:

            if name in student["name"].lower():
                display_student(student)
                found = True

        if not found:
            print("Student not found.")

    else:
        print("Invalid choice.")


# ---------------------------------------------------------
# UPDATE STUDENT
# ---------------------------------------------------------

def update_student(students):

    print("\n========== UPDATE STUDENT ==========")

    value = input("Enter student ID: ")

    if not value.isdigit():
        print("Invalid ID.")
        return

    student_id = int(value)

    student = None

    for item in students:

        if item["id"] == student_id:
            student = item
            break

    if student is None:
        print("Student not found.")
        return

    print("\nStudent found:")
    display_student(student)

    print("\nWhat do you want to update?")
    print("1. Name")
    print("2. Age")
    print("3. Course")
    print("4. Marks")

    choice = input("Enter choice: ")

    if choice == "1":

        new_name = input("Enter new name: ").strip()

        if new_name:
            student["name"] = new_name
            print("Name updated successfully.")

    elif choice == "2":

        new_age = input("Enter new age: ")

        if new_age.isdigit():
            student["age"] = int(new_age)
            print("Age updated successfully.")

        else:
            print("Invalid age.")

    elif choice == "3":

        new_course = input("Enter new course: ").strip()

        if new_course:
            student["course"] = new_course
            print("Course updated successfully.")

    elif choice == "4":

        for subject in student["marks"]:

            while True:

                value = input(
                    f"Enter new marks for {subject}: "
                )

                try:

                    mark = float(value)

                    if 0 <= mark <= 100:
                        student["marks"][subject] = mark
                        break

                    else:
                        print("Marks must be between 0 and 100.")

                except ValueError:
                    print("Invalid marks.")

        average = calculate_average(student["marks"])

        student["average"] = round(average, 2)
        student["grade"] = calculate_grade(average)

        print("Marks updated successfully.")

    else:
        print("Invalid choice.")
        return

    save_students(students)


# ---------------------------------------------------------
# DELETE STUDENT
# ---------------------------------------------------------

def delete_student(students):

    print("\n========== DELETE STUDENT ==========")

    value = input("Enter student ID: ")

    if not value.isdigit():
        print("Invalid ID.")
        return

    student_id = int(value)

    for student in students:

        if student["id"] == student_id:

            display_student(student)

            confirmation = input(
                "\nAre you sure you want to delete this student? (yes/no): "
            ).lower()

            if confirmation == "yes":

                students.remove(student)

                save_students(students)

                print("Student deleted successfully.")

            else:

                print("Deletion cancelled.")

            return

    print("Student not found.")


# ---------------------------------------------------------
# CLASS STATISTICS
# ---------------------------------------------------------

def statistics(students):

    print("\n========== CLASS STATISTICS ==========")

    if not students:
        print("No student data available.")
        return

    averages = [
        student["average"]
        for student in students
    ]

    class_average = sum(averages) / len(averages)

    highest = max(
        students,
        key=lambda student: student["average"]
    )

    lowest = min(
        students,
        key=lambda student: student["average"]
    )

    passed = 0
    failed = 0

    for student in students:

        if student["average"] >= 50:
            passed += 1
        else:
            failed += 1

    print("Total students :", len(students))
    print("Class average  :", round(class_average, 2))

    print("\nHighest scorer:")
    print("Name:", highest["name"])
    print("Average:", highest["average"])

    print("\nLowest scorer:")
    print("Name:", lowest["name"])
    print("Average:", lowest["average"])

    print("\nPassed:", passed)
    print("Failed:", failed)


# ---------------------------------------------------------
# SORT STUDENTS
# ---------------------------------------------------------

def sort_students(students):

    print("\n========== SORT STUDENTS ==========")

    if not students:
        print("No students available.")
        return

    print("1. Sort by name")
    print("2. Sort by average")
    print("3. Sort by ID")

    choice = input("Enter choice: ")

    if choice == "1":

        sorted_students = sorted(
            students,
            key=lambda student: student["name"].lower()
        )

    elif choice == "2":

        sorted_students = sorted(
            students,
            key=lambda student: student["average"],
            reverse=True
        )

    elif choice == "3":

        sorted_students = sorted(
            students,
            key=lambda student: student["id"]
        )

    else:

        print("Invalid choice.")
        return

    for student in sorted_students:
        display_student(student)


# ---------------------------------------------------------
# MENU
# ---------------------------------------------------------

def menu():

    students = load_students()

    while True:

        print("\n")
        print("======================================")
        print("       STUDENT MANAGEMENT SYSTEM")
        print("======================================")

        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Class Statistics")
        print("7. Sort Students")
        print("8. Exit")

        print("======================================")

        choice = input("Enter your choice: ")

        if choice == "1":

            add_student(students)

        elif choice == "2":

            view_students(students)

        elif choice == "3":

            search_student(students)

        elif choice == "4":

            update_student(students)

        elif choice == "5":

            delete_student(students)

        elif choice == "6":

            statistics(students)

        elif choice == "7":

            sort_students(students)

        elif choice == "8":

            print("\nSaving data...")

            save_students(students)

            print("Thank you for using the system!")
            break

        else:

            print("Invalid choice. Please try again.")


# ---------------------------------------------------------
# PROGRAM START
# ---------------------------------------------------------

if __name__ == "__main__":
    menu()