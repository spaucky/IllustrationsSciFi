#this locates files with the wrong file formats or files which are not images

from pathlib import Path
import imghdr

def false_image_finder(file):
    data_dir = ("data/" + file)
    image_extensions = [".png", ".jpg", ".jpeg"]  # add there all your images file extensions
    
    img_type_accepted_by_tf = ["bmp", "gif", "jpeg", "png"]
    for filepath in Path(data_dir).rglob("*"):
        if filepath.suffix.lower() in image_extensions:
            img_type = imghdr.what(filepath)
            if img_type is None:
                print(f"{filepath} is not an image")
            elif img_type not in img_type_accepted_by_tf:
                print(f"{filepath} is a {img_type}, not accepted by TensorFlow")
                
false_image_finder('PlantScientific')
