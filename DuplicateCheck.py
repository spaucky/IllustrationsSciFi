import hashlib
import os

def duplicate_remover(file_name):
    hashes = set()

    files_before = next(os.walk(file_name))[2] #the folder name can be changed here and after

    #runs through the images and if the image has an unrecognised hash - adds it to a set of hashes which future images are checked against
    for filename in os.listdir(file_name):
        path = os.path.join(file_name, filename)
        digest = hashlib.sha1(open(path,'rb').read()).digest()
        if digest not in hashes:
            hashes.add(digest)
        else:
            os.remove(path)
        
    files_after = next(os.walk(file_name))[2] #directory is your directory path as string
    return len(files_before) == len(files_after)
#check that there is the same number of images before and after
duplicate_remover('PlantScientific')
#removed 2 images from PlantArt
#removed 2 images from PlantScientific
