import os
import glob


def find(directory, keywords, extensions, output_file=None, ignore_folders=None):
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
                    if any(keyword in content for keyword in keywords):
                        out_file.write(f"{file_path}\n")
            except Exception as e:
                print(f"Could not read file {file_path}: {e}")


if __name__ == "__main__":
    #! INPUT
    folder_path = r"C:\Users\vvn20206205\Downloads\Nghia\Git\whynotnghiavu\VideoVN"
    folder_path = r"C:\Users\vvn20206205\Downloads\Nghia\Git"
    keywords = [

        # "replace",
        # "MyNewPath",

        #  "NOTE",

        # "os.path.exists",
        #  "MyLog",


        #  "ChuyenAmThanh",

        #  "🐍",

        # "#",


        #  "print",
        "link",
        # "encoding",




    ]
    extensions = [
        ".py",
        ".md",
                  ]
    output_file = "output.md"
    ignore_folders = [
        ".git",
        "node_modules",
        "__pycache__"
    ]
#! INPUT

    with open(output_file, 'w', encoding="utf-8") as file:
        file.write(f"PATH: {folder_path}\nKeywords: {keywords}\n\n\n")
    find(folder_path, keywords, extensions, output_file=output_file, ignore_folders=ignore_folders)
    print(f"Kết quả đã được ghi vào tập tin {output_file}")
