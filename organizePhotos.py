import os

# path = os.path.join("c:\\", "Users", "VAMSI", "Desktop", "Python")
source = os.path.abspath(os.path.join(os.sep, "Users", "VAMSI", "Desktop", "Python"))
print(source)
os.chdir(source)
# os.chdir("c:\\Users\VAMSI\Desktop\Python\organize photos")
files = os.listdir()
print(files)

# filename = "sample.txt"
# new_path = "Photos"
# os.rename(filename, os.path.join(new_path, filename))
