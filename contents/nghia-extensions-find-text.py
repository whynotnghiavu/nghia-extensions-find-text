import os
import glob



def find(directory, keywords, extensions,   output_file=None, ignore_folders=None): 
    files = []
    for extension in extensions:
        files +=    glob.glob(os.path.join(directory, f'**/*{extension}'), recursive=True)
    print(files)





    
# 
 
    #         if os.path.basename(item_path) not in ignore_folders:



    with open(output_file, "a", encoding="utf-8") as file:
        file.write( path+ "\n")

     








#! INPUT
keywords = "#"
keywords = "NOTE"
keywords = "print"
keywords = "replace"


extensions = [
    ".py",
]


folder_path = r"C:\Users\vvn20206205\Downloads\Nghia\Git\whynotnghiavu\VideoVN" 

output_file = "output.txt"
ignore_folders = [
    ".git", 
    "node_modules", 
    "__pycache__"
]
#! INPUT
with open(output_file, 'w', encoding="utf-8") as file:
    file.write(f"PATH: {folder_path}\nKeywords: {keywords}\n\n\n")

find(folder_path,  keywords,   extensions  ,  output_file=output_file, ignore_folders=ignore_folders)
print(f"Kết quả đã được ghi vào tập tin {output_file}")
