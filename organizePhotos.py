import os

path = os.path.join("c:\\", "Users", "VAMSI", "Desktop", "Python")
print(path)
os.chdir(path)
files = os.listdir()
print(files)
