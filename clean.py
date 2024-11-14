import os
import shutil

EXCLUDED_DIRS = [
    ".venv",
    ".git",
]  # exclude __pycache__ directories inside these folders
DIRS_TO_DELETE = ["__pycache__"]


def delete_folders(
    folders: list = DIRS_TO_DELETE, exclude: list = EXCLUDED_DIRS, path: str = "."
) -> None:
    print("Cleaning...")
    for root, _, _ in os.walk(path):
        try:
            root_dir = root.split(os.sep)[1]
            end_dir = root.rsplit(os.sep, 1)[1]

            if root_dir not in exclude and end_dir in folders:
                print(root)

                try:
                    shutil.rmtree(root)
                except (PermissionError, FileNotFoundError):
                    pass

        except IndexError:  # root dir
            pass
        except Exception as e:
            print(e)
    print("Done.")
