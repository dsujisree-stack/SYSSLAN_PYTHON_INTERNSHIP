import csv

file_name = "student_data.csv"

print("\n======= SMART CSV READER =======\n")


def create_sample_csv():

    with open(
        file_name,
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Name",
            "Marks"
        ])

        writer.writerow([
            "Sri",
            "92"
        ])

        writer.writerow([
            "Ravi",
            "85"
        ])

        writer.writerow([
            "Anu",
            "78"
        ])

    print(
        "\n✅ Sample CSV Created!"
    )


def read_csv_data():

    print(
        "\n====== STUDENT DATA REPORT ======\n"
    )

    try:

        with open(
            file_name,
            "r"
        ) as file:

            reader = csv.reader(
                file
            )

            next(reader)

            total_students = 0
            highest_marks = 0
            topper_name = ""

            for row in reader:

                student_name = row[0]
                student_marks = int(
                    row[1]
                )

                print(
                    f"Name : "
                    f"{student_name}"
                )

                print(
                    f"Marks : "
                    f"{student_marks}"
                )

                print(
                    "----------------"
                )

                total_students += 1

                if (
                    student_marks
                    >
                    highest_marks
                ):

                    highest_marks = (
                        student_marks
                    )

                    topper_name = (
                        student_name
                    )

            print(
                f"\nTopper : "
                f"{topper_name}"
            )

            print(
                f"Highest Marks : "
                f"{highest_marks}"
            )

            print(
                f"Total Students : "
                f"{total_students}"
            )

    except FileNotFoundError:

        print(
            "⚠️ CSV file not found!"
        )


while True:

    print("\n1. Create CSV File")
    print("2. Read CSV Data")
    print("3. Exit")

    selected_option = input(
        "Choose option: "
    )

    if selected_option == "1":
        create_sample_csv()

    elif selected_option == "2":
        read_csv_data()

    elif selected_option == "3":
        print(
            "\nCSV Reader Closed!"
        )
        break

    else:
        print(
            "\n⚠️ Invalid Option!"
        )
