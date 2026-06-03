import shutil
import os
from datetime import datetime

print("\n======= SMART BACKUP SYSTEM =======\n")

source_folder = input(
    "Enter folder path to backup: "
)

try:

    if os.path.exists(
        source_folder
    ):

        current_time = datetime.now()

        backup_folder_name = (
            "Backup_"
            +
            current_time.strftime(
                "%d_%m_%Y_%H_%M_%S"
            )
        )

        backup_location = os.path.join(
            os.path.dirname(
                source_folder
            ),
            backup_folder_name
        )

        shutil.copytree(
            source_folder,
            backup_location
        )

        print(
            "\n✅ Backup Created Successfully!"
        )

        print(
            f"Backup Name : "
            f"{backup_folder_name}"
        )

        print(
            f"Backup Location : "
            f"{backup_location}"
        )

    else:

        print(
            "\n⚠️ Folder not found!"
        )

except Exception as error:

    print(
        f"\nError : {error}"
    )
