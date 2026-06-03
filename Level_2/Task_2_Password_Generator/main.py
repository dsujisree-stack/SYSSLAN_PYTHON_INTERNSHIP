import random
import string

saved_passwords = []

print("\n======= SECURE PASSWORD CREATOR =======\n")


def create_password():

    account_name = input(
        "Enter account name: "
    )

    try:
        password_length = int(
            input("Enter password length: ")
        )

    except ValueError:
        print("⚠️ Numbers only allowed!")
        return

    available_characters = (
        string.ascii_letters +
        string.digits
    )

    generated_password = ""

    for _ in range(password_length):
        generated_password += random.choice(
            available_characters
        )

    strength_score = 0

    if password_length >= 8:
        strength_score += 1

    if any(
        letter.isdigit()
        for letter in generated_password
    ):
        strength_score += 1

    if any(
        letter.isalpha()
        for letter in generated_password
    ):
        strength_score += 1

    saved_passwords.append(
        generated_password
    )

    print("\n====== Password Report ======")
    print(
        f"Account : {account_name}"
    )
    print(
        f"Generated Password : "
        f"{generated_password}"
    )

    if strength_score == 3:
        print("Strength : Strong ✅")
    else:
        print("Strength : Medium ⚠️")

    print(
        f"Saved Password Count : "
        f"{len(saved_passwords)}"
    )


create_password()
