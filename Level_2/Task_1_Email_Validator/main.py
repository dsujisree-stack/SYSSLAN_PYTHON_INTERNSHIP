print("\n======= SMART EMAIL INSPECTOR =======\n")

email_input = input(
    "Enter your email address: "
).strip()

validation_status = True
problem_message = ""

if "@" not in email_input:
    validation_status = False
    problem_message = "Missing @ symbol"

elif "." not in email_input:
    validation_status = False
    problem_message = "Missing domain extension"

elif email_input.startswith("@"):
    validation_status = False
    problem_message = "Email cannot start with @"

elif " " in email_input:
    validation_status = False
    problem_message = "Spaces are not allowed"

username = email_input.split("@")[0]

print("\n====== Validation Report ======\n")

if validation_status:

    print("✅ Valid Email Address")
    print(f"Username Length : {len(username)}")

    if "gmail.com" in email_input:
        print("Provider : Gmail")

    elif "yahoo.com" in email_input:
        print("Provider : Yahoo")

    elif "outlook.com" in email_input:
        print("Provider : Outlook")

    else:
        print("Provider : Custom Domain")

else:
    print("❌ Invalid Email Address")
    print("Reason :", problem_message)
