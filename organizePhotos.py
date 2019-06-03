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
    return filename.split('_')[1]

originals = ['2018-01-03_Scotland_21:51:57.jpg',
             '2016-09-04_Berlin_08:25:50.jpg',
             '2018-08-01_Oahu_21:51:37.jpg']

print(originals)

places = []
for filename in originals:
    place = extract_place(filename)
    places.append(place)

print(places)
