import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import numpy as np
import os
from PIL import Image
import matplotlib.patches as mpatches
import pandas as pd

#reading in data
image_df = pd.read_csv(os.path.join('OurDrawings','OurDrawingsScores.csv'))

#creating font
font_dictionary = {'family': 'Arial', 'color': 'black', 'weight': 'normal', 'size': 25,}

"""
I NEED TO SORT THE IMAGES SO THAT THEY HAVE THE CORRECT VALUES AND ARE IN THE CORRECT ORDER
"""

x_values = np.arange(1,13,1)
y_values = image_df['values']

#creating list of file paths to access the images
image_paths = os.listdir(os.path.join('OurDrawings','images'))[1:]
image_paths = ['OurDrawings/images/' + image for image in image_paths]

# Create a figure and axis
fig, ax = plt.subplots(figsize=(20,10))

# Scatter plot points
scatter = ax.scatter(x_values, y_values, s=10, marker='o')

# Plot images on each point
for x, y, img_path, colour in zip(x_values, y_values, image_paths, image_df['ScientificOrNot']):
    img = Image.open(img_path)
    #converting images to squares for the plot
    sqrDims = np.ceil(np.sqrt(img.size[0]*img.size[1])).astype(int)
    resize = img.resize((sqrDims, sqrDims))
    #creating squares to act as frames
    square_length = resize.size[0] + 70
    square_img = Image.new("RGB", (square_length, square_length), color=colour)
    
    #pasting the image onto the frame
    square_img.paste(resize, (32,32))
    
    #converting square and image to form where they can be plotted
    framed_images = OffsetImage(square_img, zoom=0.08, alpha=0.95)
    
    #plotting them
    
    #plotted_images = AnnotationBbox(imagebox, (x, y), frameon=False, pad=0)
    plotted_framed_images = AnnotationBbox(framed_images, (x, y), frameon=False, pad=0)
    ax.add_artist(plotted_framed_images)
    


#im_resize = im.resize((sqrWidth, sqrWidth))


# Customize the plot if needed
ax.set_title('Illustrations with Scores',fontdict=font_dictionary)
ax.set_xlabel('Order of Entries', fontdict=font_dictionary)
ax.set_ylabel("Model's Scores", fontdict=font_dictionary)
ax.set_ylim([-0.2,1.2])
ax.set_yticks(np.arange(0,1.1,0.2))
ax.set_xlim([-0.2,12.9])
ax.set_xticks(np.arange(1,13,1))
ax.tick_params(axis='x', labelsize=16)
ax.tick_params(axis='y', labelsize=16)

#creating line at 0.5 to show differentiating line
ax.plot([-1,13],[0.5,0.5], linestyle='--', c='grey', alpha=0.7)

#Creating custom legends
legend_patches = [mpatches.Patch(color='red', label='Labelled Scientific Illustration', alpha = 0.5), mpatches.Patch(color='blue', label='Labelled Art', alpha = 0.5),mpatches.Patch(color='grey', label='Binary Classification Threshold', alpha = 0.7)]
ax.legend(handles=legend_patches, loc='upper left', prop={'size': 16})
plt.show();
