import shutil
import os

sourc_file = r"C:\Users\HP\Downloads\Aakansha_Shrivastava.docx"
destination_folder = r"C:\Users\HP\Desktop\Resume"

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

destination_file = os.path.join(destination_folder, os.path.basename(source_file))

try:
  shutil.copy(source_file,destination_file)
  print(f"file copied successfully" to {destination_file})
except fileNotFoundError:
  print("source file not found:Please check the path)
except Exception as e:
  print(f"an error occurre: {e}"
