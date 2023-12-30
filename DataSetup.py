import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout
import os
import numpy as np
from matplotlib import pyplot as plt

data = tf.keras.utils.image_dataset_from_directory('data')

#loading RGB values as between 0 and 1, leaving the image identifiers the same
data = data.map(lambda x,y: (x/255, y))

data_iterator = data.as_numpy_iterator()

batch = data_iterator.next()

#setting RGB values between 0 and 1
#batches have two channels: in 0 are groups of 32 images, in 1 are the images identifiers


 
#1 Label is Scientific
#0 Label is Art

#total number of batches = 45
print(len(data))

#Using a 70%, 20% and 10% train, validation, test split
train_size = int(len(data)*0.7) #31 batches of training data
validation_size = int(len(data)*0.2) #9 batches of validation data
test_size = int(len(data)*0.1)+1 #5 batches of testing data

#assigning these batch sizes to create our split
train = data.take(train_size)
validation = data.skip(train_size).take(validation_size)
test = data.skip(train_size+validation_size).take(test_size)


