file_name = "daily_notes.txt"

print("\n======= SMART FILE READER =======\n")


def create_sample_file():

    with open(file_name, "w") as file:

        file.write(
            "Python Internship Started\n"
        )

        file.write(
            "Completed Level 1 Tasks\n"
        )

        file.write(
            "Learning File Handling\n"
        )

    print(
        "✅ Sample File Created!"
    )


def read_file_safely():

    print(
        "\n====== FILE CONTENT ======\n"
    )

    try:

        with open(file_name, "r") as file:

            total_lines = 0

            for line_number, line in enumerate(
                file,
                start=1
            ):

                print(
                    f"{line_number}. "
                    f"{line.strip()}"
                )

                total_lines += 1

            print(
                f"\nTotal Lines: "
                f"{total_lines}"
            )

    except FileNotFoundError:

        print(
            "⚠️ File not found!"
        )


while True:

    print("\n1. Create Sample File")
    print("2. Read File")
    print("3. Exit")

    user_choice = input(
        "Choose option: "
    )

    if user_choice == "1":
        create_sample_file()

    elif user_choice == "2":
        read_file_safely()

    elif user_choice == "3":
        print(
            "\nProgram Closed!"
        )
        break

    else:
        print(
            "\nInvalid Option!"
        )
