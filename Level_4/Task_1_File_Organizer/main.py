import os
import shutil

print("\n======= SMART FILE ORGANIZER =======\n")

source_folder = input(
    "Enter folder path: "
)

file_categories = {
    "Images": [".jpg", ".png", ".jpeg"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"]
}

moved_files = 0

try:

    all_files = os.listdir(
        source_folder
    )

    for single_file in all_files:

        file_path = os.path.join(
            source_folder,
            single_file
        )

        if os.path.isfile(
            file_path
        ):

            file_extension = os.path.splitext(
                single_file
            )[1].lower()

            for folder_name, extensions in (
                file_categories.items()
            ):

                if (
                    file_extension
                    in
                    extensions
                ):

                    target_folder = (
                        os.path.join(
                            source_folder,
                            folder_name
                        )
                    )

                    os.makedirs(
                        target_folder,
                        exist_ok=True
                    )

                    shutil.move(
                        file_path,
                        os.path.join(
                            target_folder,
                            single_file
                        )
                    )

                    moved_files += 1
                    break

    print(
        f"\n✅ Total Organized Files: "
        f"{moved_files}"
    )

except FileNotFoundError:

    print(
        "⚠️ Folder not found!"
    )
