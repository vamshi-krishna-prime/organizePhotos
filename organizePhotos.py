import os

def extract_place(filename):
    return filename.split("_")[1]

def make_directories(list):
    for location in list:
        os.mkdir(location)

# navigating to the photos directory and listing the file names
os.chdir("c:\\Users\VAMSI\Desktop\Python\organize photos\Photos")
originals = os.listdir()
print(originals)
places = []
# loop to extract place names
for filename in originals:
    place_name = extract_place(filename)
    if place_name not in places:
        places.append(place_name)

print(places)
make_directories(places)

for filename in originals:
    place_name = extract_place(filename)
    os.rename(filename, os.path.join(place_name, filename))
