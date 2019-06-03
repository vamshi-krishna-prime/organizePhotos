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

def extract_place(filename):
    first = filename.find("_")
    partial = filename[first + 1 : ]
    second = partial.find("_")
    folder_name = partial[:second]
    return folder_name
  
print(extract_place("2016-11-04_Berlin_09/42/22.jpg"))
print(extract_place("2018-01-03_Oahu_21/51/57.jpg"))
print(extract_place("2018-01_Scottland_11/51/27.jpg"))
