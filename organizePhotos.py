import os

def extract_place(filename):
    return filename.split("_")[1]

def make_directories(list):
    for location in list:
        os.mkdir(location)

def organize_photos(directory):
    os.chdir(directory)
    originals = os.listdir()
    print(originals)
    places = []
    # loop to extract place names
    for filename in originals:
        place_name = extract_place(filename)
        if place_name not in places:
            places.append(place_name)
    # print the list of places and make directories
    print(places)
    make_directories(places)
    # move/organize the photos to the respective folders
    for filename in originals:
        place_name = extract_place(filename)
        os.rename(filename, os.path.join(place_name, filename))


organize_photos("Photos")
