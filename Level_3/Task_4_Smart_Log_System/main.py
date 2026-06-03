from datetime import datetime

log_storage_file = "smart_activity_log.txt"

print("\n======= SMART ACTIVITY LOGGER =======\n")


def save_activity():

    activity_name = input(
        "Enter Activity Name: "
    )

    category_name = input(
        "Enter Category "
        "(Study/Coding/Project): "
    )

    priority_level = input(
        "Priority "
        "(High/Medium/Low): "
    )

    current_time = datetime.now()

    formatted_time = current_time.strftime(
        "%d-%m-%Y | %I:%M:%S %p"
    )

    log_information = (
        f"[{formatted_time}] | "
        f"Activity: {activity_name} | "
        f"Category: {category_name} | "
        f"Priority: {priority_level}\n"
    )

    with open(
        log_storage_file,
        "a"
    ) as file:

        file.write(
            log_information
        )

    print(
        "\n✅ Activity Logged Successfully!"
    )


def view_saved_logs():

    print(
        "\n====== SAVED ACTIVITY LOGS ======\n"
    )

    try:

        with open(
            log_storage_file,
            "r"
        ) as file:

            all_logs = (
                file.readlines()
            )

            if len(all_logs) == 0:
                print(
                    "No logs available."
                )
                return

            total_log_count = 0

            for item_number, item in enumerate(
                all_logs,
                start=1
            ):

                print(
                    f"{item_number}. "
                    f"{item.strip()}"
                )

                total_log_count += 1

            print(
                f"\nTotal Logs : "
                f"{total_log_count}"
            )

    except FileNotFoundError:

        print(
            "⚠️ No log file found!"
        )


while True:

    print("\n1. Add Activity")
    print("2. View Logs")
    print("3. Exit")

    selected_option = input(
        "Choose option: "
    )

    if selected_option == "1":
        save_activity()

    elif selected_option == "2":
        view_saved_logs()

    elif selected_option == "3":
        print(
            "\nSmart Logger Closed!"
        )
        break

    else:
        print(
            "\n⚠️ Invalid Option!"
        )
