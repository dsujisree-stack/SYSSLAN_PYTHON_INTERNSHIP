file_name = "student_records.txt"

print("\n======= FILE RECORD MANAGER =======\n")


def save_record():

    student_name = input(
        "Enter Student Name: "
    )

    roll_number = input(
        "Enter Roll Number: "
    )

    marks = input(
        "Enter Marks: "
    )

    student_data = (
        f"Name: {student_name}, "
        f"Roll No: {roll_number}, "
        f"Marks: {marks}\n"
    )

    with open(file_name, "a") as file:
        file.write(student_data)

    print(
        "\n✅ Record Saved Successfully!"
    )


def view_records():

    print(
        "\n====== SAVED RECORDS ======\n"
    )

    try:

        with open(file_name, "r") as file:

            saved_data = (
                file.readlines()
            )

            if len(saved_data) == 0:
                print(
                    "No records available."
                )
                return

            record_count = 0

            for item in saved_data:
                record_count += 1
                print(
                    f"{record_count}. "
                    f"{item.strip()}"
                )

            print(
                f"\nTotal Records: "
                f"{record_count}"
            )

    except FileNotFoundError:
        print(
            "⚠️ No file found!"
        )


while True:

    print("\n1. Save Record")
    print("2. View Records")
    print("3. Exit")

    user_choice = input(
        "Choose option: "
    )

    if user_choice == "1":
        save_record()

    elif user_choice == "2":
        view_records()

    elif user_choice == "3":
        print(
            "\nProgram Closed!"
        )
        break

    else:
        print(
            "\nInvalid Option!"
        )
