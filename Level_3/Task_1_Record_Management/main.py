student_records = []

print("\n======= SMART RECORD HUB =======\n")


def add_record():

    student_name = input(
        "Enter Student Name: "
    )

    roll_number = input(
        "Enter Roll Number: "
    )

    marks = int(
        input("Enter Marks: ")
    )

    if marks >= 90:
        grade = "A+"
    elif marks >= 75:
        grade = "A"
    elif marks >= 50:
        grade = "B"
    else:
        grade = "C"

    student_data = {
        "Name": student_name,
        "Roll": roll_number,
        "Marks": marks,
        "Grade": grade
    }

    student_records.append(
        student_data
    )

    print(
        "\n✅ Record Added Successfully!"
    )


def view_records():

    if len(student_records) == 0:
        print("\nNo records available.")
        return

    print(
        "\n====== STUDENT REPORT ======\n"
    )

    for student in student_records:
        print(student)


def search_student():

    search_name = input(
        "\nEnter name to search: "
    )

    found = False

    for student in student_records:

        if (
            student["Name"].lower()
            ==
            search_name.lower()
        ):

            print(
                "\n🎉 Student Found!"
            )
            print(student)

            found = True

    if not found:
        print(
            "❌ Student not found."
        )


while True:

    print("\n1. Add Record")
    print("2. View Records")
    print("3. Search Student")
    print("4. Exit")

    user_choice = input(
        "Choose option: "
    )

    if user_choice == "1":
        add_record()

    elif user_choice == "2":
        view_records()

    elif user_choice == "3":
        search_student()

    elif user_choice == "4":
        print(
            "\nProgram Closed!"
        )
        break

    else:
        print(
            "\nInvalid Option!"
        )
