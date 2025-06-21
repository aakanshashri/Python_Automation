import os
import shutil

dest_dir = os.path.join(os.getcwd(),"test")

if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)

src_dir = os.path.join(os.getcwd(),"sample_data","read.md")

if not os.path.exists(src_dir):
    os.mkdir(src_dir)
print(os.path.basename(src_dir))
dest_file = os.path.join(dest_dir,os.path.basename(src_dir))
shutil.move(src_dir,dest_file)
