import hashlib
import os

hashes = set()

files_before = next(os.walk('PlantArt'))[2] #the folder name can be changed here and after

#runs through the images and if the image has an unrecognised hash - adds it to a set of hashes which future images are checked against
for filename in os.listdir('PlantArt'):
    path = os.path.join('PlantArt', filename)
    digest = hashlib.sha1(open(path,'rb').read()).digest()
    if digest not in hashes:
        hashes.add(digest)
    else:
        os.remove(path)
        
files_after = next(os.walk('PlantArt'))[2] #directory is your directory path as string

#check that there is the same number of images before and after
assert len(files_before) == len(files_after)
