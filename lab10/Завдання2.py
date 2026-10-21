import os
import shutil

dst = "C:\\R_FILES"
if not os.path.exists(dst):          
    os.makedirs(dst)

files = os.listdir()                 
print("Файли поточного каталогу:")
for name in files:
    if os.path.isfile(name):         
        print(name)
        if name.lower().startswith("r"):
            shutil.copy(name, dst)   
            print("   -> скопійовано в", dst)