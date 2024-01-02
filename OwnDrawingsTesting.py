import os
import cv2
from tensorflow.keras.models import load_model
import tensorflow as tf
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

testing_model = load_model(os.path.join('models','ImprovedNeuralNetwork.h5'))
yhat_list = []

for image in os.listdir(os.path.join('data','OurDrawings'))[1:]:
    #reading in image
    img = cv2.imread(os.path.join('data','OurDrawings',image))
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
image_df = pd.DataFrame({'images': os.listdir(os.path.join('data','OurDrawings'))[1:], 'values': yhat_list})
image_df['ScientificOrNot'] = image_df['values'].apply(ScientificOrNotColour)

image_df.to_csv('OurDrawingsScores.csv')

