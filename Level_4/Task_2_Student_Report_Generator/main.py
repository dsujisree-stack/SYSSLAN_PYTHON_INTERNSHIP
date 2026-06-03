student_database = []

print("\n======= SMART STUDENT REPORT SYSTEM =======\n")


def add_student():

    student_name = input(
        "Enter Student Name: "
    )

    try:
        student_marks = int(
            input("Enter Marks: ")
        )

    except ValueError:
        print(
            "⚠️ Numbers only allowed!"
        )
        return

    if student_marks >= 90:
        grade = "A+"
    elif student_marks >= 75:
        grade = "A"
    elif student_marks >= 50:
        grade = "B"
    else:
        grade = "C"

    status = (
        "Pass"
        if student_marks >= 35
        else "Fail"
    )

    student_database.append({
        "name": student_name,
        "marks": student_marks,
        "grade": grade,
        "status": status
    })

    print(
        "\n✅ Student Added!"
    )


def generate_report():

    if len(student_database) == 0:
        print(
            "\nNo student data found."
        )
        return

    print(
        "\n====== STUDENT REPORT ======\n"
    )

    total_marks = 0
    highest_marks = 0
    topper_name = ""

    for student in student_database:

        print(
            f"Name: {student['name']}"
        )
        print(
            f"Marks: {student['marks']}"
        )
        print(
            f"Grade: {student['grade']}"
        )
        print(
            f"Status: {student['status']}"
        )
        print("-------------------")

        total_marks += (
            student["marks"]
        )

        if (
            student["marks"]
            >
            highest_marks
        ):

            highest_marks = (
                student["marks"]
            )

            topper_name = (
                student["name"]
            )

    average_marks = (
        total_marks
        /
        len(student_database)
    )

    print(
        f"\n🏆 Topper: "
        f"{topper_name}"
    )

    print(
        f"Highest Marks: "
        f"{highest_marks}"
    )

    print(
        f"Class Average: "
        f"{average_marks:.2f}"
    )


while True:

    print("\n1. Add Student")
    print("2. Generate Report")
    print("3. Exit")

    user_option = input(
        "Choose option: "
    )

    if user_option == "1":
        add_student()

    elif user_option == "2":
        generate_report()

    elif user_option == "3":
        print(
            "\nSystem Closed!"
        )
        break

    else:
        print(
            "\n⚠️ Invalid Option!"
        )
