import hashlib
import os

hashes = set()

files_before = next(os.walk('PlantArt'))[2] #directory is your directory path as string

for filename in os.listdir('PlantArt'):
    path = os.path.join('PlantArt', filename)
    digest = hashlib.sha1(open(path,'rb').read()).digest()
    if digest not in hashes:
        hashes.add(digest)
    else:
        os.remove(path)
        
files_after = next(os.walk('PlantArt'))[2] #directory is your directory path as string

assert files_before == files_after
