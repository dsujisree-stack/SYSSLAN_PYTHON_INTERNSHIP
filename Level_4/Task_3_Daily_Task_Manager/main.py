task_file = "daily_tasks.txt"

print("\n======= SMART DAILY TASK MANAGER =======\n")


def add_task():

    task_name = input(
        "Enter Task Name: "
    )

    task_priority = input(
        "Priority "
        "(High/Medium/Low): "
    )

    task_details = (
        f"Task: {task_name} | "
        f"Priority: {task_priority}\n"
    )

    with open(task_file, "a") as file:
        file.write(task_details)

    print(
        "\n✅ Task Saved Successfully!"
    )


def view_tasks():

    print(
        "\n====== SAVED TASKS ======\n"
    )

    try:

        with open(task_file, "r") as file:

            saved_tasks = (
                file.readlines()
            )

            if len(saved_tasks) == 0:
                print(
                    "No tasks available."
                )
                return

            task_count = 0

            for task in saved_tasks:

                task_count += 1

                print(
                    f"{task_count}. "
                    f"{task.strip()}"
                )

            print(
                f"\nTotal Tasks : "
                f"{task_count}"
            )

    except FileNotFoundError:

        print(
            "⚠️ No task file found!"
        )


while True:

    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    selected_option = input(
        "Choose option: "
    )

    if selected_option == "1":
        add_task()

    elif selected_option == "2":
        view_tasks()

    elif selected_option == "3":
        print(
            "\nTask Manager Closed!"
        )
        break

    else:
        print(
            "\n⚠️ Invalid Option!"
        )
