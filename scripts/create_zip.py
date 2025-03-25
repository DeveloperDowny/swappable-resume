import os
import zipfile
from pathlib import Path


def zip_folder(source_folder: str, output_zip: str) -> None:
    """
    Compresses the contents of a folder into a zip file.

    Args:
        source_folder (str): The path to the folder to be zipped.
        output_zip (str): The path to the output zip file.
    """
    validate_paths(source_folder, output_zip)

    with zipfile.ZipFile(output_zip, "w", zipfile.ZIP_DEFLATED) as zip_file:
        for folder_name, subfolders, filenames in os.walk(source_folder):
            for filename in filenames:
                file_path = os.path.join(folder_name, filename)
                arcname = os.path.relpath(file_path, source_folder)
                zip_file.write(file_path, arcname)
    print(f"Folder '{source_folder}' has been zipped to '{output_zip}'.")


def validate_paths(source_folder: str, output_zip: str) -> None:
    """
    Validates the source folder and output zip file paths.

    Args:
        source_folder (str): The path to the folder to be zipped.
        output_zip (str): The path to the output zip file.

    Raises:
        ValueError: If the source folder does not exist or is not a directory.
    """
    if not os.path.exists(source_folder):
        raise ValueError(f"Source folder '{source_folder}' does not exist.")
    if not os.path.isdir(source_folder):
        raise ValueError(f"Source folder '{source_folder}' is not a directory.")
    output_dir = Path(output_zip).parent
    if not output_dir.exists():
        raise ValueError(f"Output directory '{output_dir}' does not exist.")


def main() -> None:
    """
    Main function to execute the script.
    """
    # source_folder = input("Enter the path to the folder to zip: ").strip()
    # output_zip = input("Enter the path for the output zip file: ").strip()

    source_folder = "latex-code"
    output_zip = "resume.zip"

    try:
        zip_folder(source_folder, output_zip)
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
