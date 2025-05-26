import os
import shutil
from datetime import  datetime

#folder_path = r"C:\Users\HP\Documents\Test_Folder"

timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
print(timestamp)

def rename_file(folder_path):
    for file in  os.listdir(folder_path):
        oldfilename = file
        filename = os.path.splitext(file)[0]
        print(filename)
        file_ext = os.path.splitext(file)[1]
        file_extn = file_ext[:5]
        print(file_extn)
        newname = filename.replace(' ','_') + file_extn
        print(newname)
        src = os.path.join(folder_path, oldfilename)
        print(src)
        dest = os.path.join(folder_path, newname)
        print(dest)
        os.rename(src,dest)

    print("name renamed successfully")

def main():
    folder_path = input("Please enter your folder path")
    print(folder_path)
    rename_file(folder_path)

if __name__ == "__main__":
    main()
