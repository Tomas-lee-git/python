"""
    1. binary file:
        1). just zeros and ones;
        2). can be laid out in any pattern you might want particularly:graphical,video,audio;
        
    2. pillow: the Python Imaging Library
        1). docs: pillow.readthedocs.io;
        2). Image.open(file_path), enhance image ability;
    
    3. gif: 
        enough images it creates the illusion of Animation;

    4. 

"""
import sys

from PIL import Image

images = []

for arg in sys.argv[1:]: # list[start:end], get everything except the first thing
    images.append(Image.open(arg))

# print(images)

images[0].save(
    "costumes.gif", # new image's name
    save_all = True, # save all of the frames
    append_images = [images[1]], # specify following images with list
    duration = 200, # milliseconds for each of these frames
    loop = 0, # infinite number of times loop
)