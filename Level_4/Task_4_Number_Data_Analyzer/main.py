data_file = "student_scores.txt"

print("\n======= SMART NUMBER ANALYZER =======\n")


def create_sample_data():

    with open(data_file, "w") as file:

        file.write("45\n")
        file.write("78\n")
        file.write("92\n")
        file.write("66\n")
        file.write("88\n")

    print(
        "\n✅ Sample Data File Created!"
    )


def analyze_numbers():

    print(
        "\n====== NUMBER REPORT ======\n"
    )

    try:

        with open(data_file, "r") as file:

            number_list = []

            for line in file:
                number_list.append(
                    int(line.strip())
                )

            if len(number_list) == 0:
                print(
                    "No numbers available."
                )
                return

            total_score = sum(
                number_list
            )

            average_score = (
                total_score
                /
                len(number_list)
            )

            highest_score = max(
                number_list
            )

            lowest_score = min(
                number_list
            )

            print(
                f"Numbers : "
                f"{number_list}"
            )

            print(
                f"Total : "
                f"{total_score}"
            )

            print(
                f"Average : "
                f"{average_score:.2f}"
            )

            print(
                f"Highest : "
                f"{highest_score}"
            )

            print(
                f"Lowest : "
                f"{lowest_score}"
            )

            print(
                f"Count : "
                f"{len(number_list)}"
            )

    except FileNotFoundError:

        print(
            "⚠️ File not found!"
        )


while True:

    print("\n1. Create Sample File")
    print("2. Analyze Data")
    print("3. Exit")

    selected_option = input(
        "Choose option: "
    )

    if selected_option == "1":
        create_sample_data()

    elif selected_option == "2":
        analyze_numbers()

    elif selected_option == "3":
        print(
            "\nAnalyzer Closed!"
        )
        break

    else:
        print(
            "\n⚠️ Invalid Option!"
        )
