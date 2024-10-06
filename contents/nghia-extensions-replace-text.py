import os
import glob


def find_and_replace(directory, keywords, replacements, extensions, output_file=None, ignore_folders=None):
    files = []
    for extension in extensions:
        files += glob.glob(os.path.join(directory, f'**/*{extension}'), recursive=True)

    if ignore_folders:
        files = [file for file in files if not any(ig in file for ig in ignore_folders)]

    with open(output_file, "a", encoding="utf-8") as out_file:
        for file_path in files:
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    updated = False
                    for keyword, replacement in zip(keywords, replacements):
                        if keyword in content:
                            content = content.replace(keyword, replacement)
                            updated = True

                    if updated:
                        with open(file_path, "w", encoding="utf-8") as f_out:
                            f_out.write(content)
                        out_file.write(f"Updated: {file_path}\n")

            except Exception as e:
                print(f"Could not read file {file_path}: {e}")


if __name__ == "__main__":
    #! INPUT
    folder_path = r"C:\Users\vvn20206205\Downloads\Nghia\Git\whynotnghiavu\FIS-otp-3\contents\code"

    keywords = [
# "from code.backend.app.auth.auth_handler import AuthHandler"
"from code.backend.app.auth.utils.auth_handler import AuthHandler"
    ]
    replacements = [
# "from app.auth.auth_handler import AuthHandler"
"from app.auth.utils.auth_handler import AuthHandler"
    ]
    
    extensions = [
        ".py",
        ".md",
    ]
    output_file = "output_replace.md"
    ignore_folders = [
        ".git",
        "node_modules",
        "__pycache__"
    ]
    #! INPUT

    with open(output_file, 'w', encoding="utf-8") as file:
        file.write(f"PATH: {folder_path}\nKeywords: {keywords}\nReplacements: {replacements}\n\n\n")
    
    find_and_replace(folder_path, keywords, replacements, extensions, output_file=output_file, ignore_folders=ignore_folders)
    print(f"Replacements have been recorded in {output_file}")
