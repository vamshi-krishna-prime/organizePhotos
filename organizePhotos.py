import os

source = os.path.abspath(os.path.join(os.sep, "Users", "VAMSI", "Desktop", "Python"))
print(source)
os.chdir(source)
files = os.listdir()
print(files)

os.chdir("c:\\Users\VAMSI\Desktop\Python\organize photos")
filename = "sample.txt"
path = "Photos"
os.rename(filename, os.path.join(path, filename))
