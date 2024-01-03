import os
import cv2
from tensorflow.keras.models import load_model
import tensorflow as tf
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

#creating list of image paths
image_paths = os.listdir(os.path.join('OurDrawings','Images'))
if '.DS_Store' in os.listdir(os.path.join('OurDrawings','Images')):
    image_paths.remove('.DS_Store')

    
print(image_paths)


testing_model = load_model(os.path.join('models','ImprovedNeuralNetwork.h5'))
yhat_list = []

for image in image_paths:
    #reading in image
    img = cv2.imread(os.path.join('OurDrawings','Images',image))
    #converting image to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #resizing the image to 256x256
    resize = tf.image.resize(img, (256,256))
    yhat = testing_model.predict(np.expand_dims(resize/255, 0))
    yhat_list.append(yhat[0][0])
    plt.imshow(img)
    plt.title(f"{image[:-5]}: {str(yhat)[2:-2]}")
    plt.show()
    
def ScientificOrNotColour(x):
    if x > 0.5:
        return 'red'
    else:
        return 'blue'
image_df = pd.DataFrame({'images': image_paths, 'values': yhat_list})
image_df['ScientificOrNot'] = image_df['values'].apply(ScientificOrNotColour)

#creating a column which assigns the 'order of log entries' to the dataframe
ordering_dict = {'Latcher1.jpeg': 1, 
                'Bubbles2.jpeg': 2,
                'Bubbles1.jpeg': 3,
                'Colourful.jpeg': 4,
                'Tendrils.jpeg': 5,
                'NightVision.png': 6,
                'Burrowers2.jpeg': 7,
                'Burrowers1.jpeg': 8,
                'Engulfers2.jpeg': 9,
                'Engulfers1.jpeg': 10,
                'Bubbles3.jpeg': 11,
                'Tumblers1.jpeg': 12,
                'StaticPoppers.png': 13,
                'System1.jpeg': 14}

image_df.index = image_df['images'].map(ordering_dict)
image_df = image_df.sort_index()


image_df.to_csv('OurDrawingsScores.csv')
