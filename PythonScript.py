import os
import shutil
dir1='C:/Project/'
dir2='D:/Script/'

for file in os.listdir(dir1):
    print("Please wait!! The file is moving")
    #shutil.copy2(dir1 +file , dir2+file)
    shutil.move(dir1 +file , dir2+file)
