import random
import string

notes_file = "personal_notes.txt"

print("\n======= PERSONAL PRODUCTIVITY HUB =======\n")


def save_note():

    user_note = input(
        "Write your note: "
    )

    with open(
        notes_file,
        "a"
    ) as file:

        file.write(
            user_note + "\n"
        )

    print(
        "\n✅ Note Saved!"
    )


def view_notes():

    print(
        "\n====== SAVED NOTES ======\n"
    )

    try:

        with open(
            notes_file,
            "r"
        ) as file:

            saved_notes = (
                file.readlines()
            )

            if len(saved_notes) == 0:
                print(
                    "No notes found."
                )
                return

            for note_number, note in enumerate(
                saved_notes,
                start=1
            ):

                print(
                    f"{note_number}. "
                    f"{note.strip()}"
                )

    except FileNotFoundError:

        print(
            "⚠️ No notes file found!"
        )


def generate_password():

    try:

        password_length = int(
            input(
                "Password Length: "
            )
        )

        all_characters = (
            string.ascii_letters
            +
            string.digits
        )

        password = ""

        for _ in range(
            password_length
        ):

            password += (
                random.choice(
                    all_characters
                )
            )

        print(
            f"\n🔐 Password: "
            f"{password}"
        )

    except ValueError:

        print(
            "⚠️ Enter numbers only!"
        )


def save_daily_goal():

    goal = input(
        "Enter today's goal: "
    )

    with open(
        notes_file,
        "a"
    ) as file:

        file.write(
            f"Goal: {goal}\n"
        )

    print(
        "\n🎯 Goal Saved!"
    )


while True:

    print("\n1. Save Note")
    print("2. View Notes")
    print("3. Generate Password")
    print("4. Save Daily Goal")
    print("5. Exit")

    user_choice = input(
        "Choose option: "
    )

    if user_choice == "1":
        save_note()

    elif user_choice == "2":
        view_notes()

    elif user_choice == "3":
        generate_password()

    elif user_choice == "4":
        save_daily_goal()

    elif user_choice == "5":
        print(
            "\nProductivity Hub Closed!"
        )
        break

    else:
        print(
            "\n⚠️ Invalid Option!"
        )
