import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, BatchNormalization, Dropout
from matplotlib import plt
import os

#setting up the data


model = Sequential()
model.add(Conv2D(16, (3,3), 1, activation='relu', input_shape=(256,256,3)))
model.add(BatchNormalization())
model.add(MaxPooling2D())

model.add(Conv2D(32, (3,3), 1, activation='relu'))
model.add(Dropout(0.3))
model.add(BatchNormalization())
model.add(MaxPooling2D())

model.add(Conv2D(16, (3,3), 1, activation='relu'))
model.add(Dropout(0.3))
model.add(BatchNormalization())
model.add(MaxPooling2D())

model.add(Flatten())

model.add(Dense(256, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile('adam', loss=tf.losses.BinaryCrossentropy(), metrics=[tf.keras.metrics.BinaryAccuracy()])
model.summary()

tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir='logs')
# .fit is the training portion, we give it our training data, state the number of times it should run through this
hist = model.fit(train, epochs=30, validation_data=validation, callbacks=[tensorboard_callback])

#saving model
model.save(os.path.join('models','ImprovedNeuralNetwork.h5'))


fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 4))

# Plot Binary Accuracy and Validation Binary Accuracy
axes[0].plot(hist.history['binary_accuracy'], color='teal', label='Binary Accuracy')
axes[0].plot(hist.history['val_binary_accuracy'], color='orange', label='Validation Binary Accuracy')
axes[0].set_title('wAccuracies')
axes[0].set_ylabel('Accuracy')
axes[0].set_xlabel('Epoch')
axes[0].set_xlim([0, 30])
axes[0].legend()

# Plot Loss and Validation Loss
axes[1].plot(hist.history['loss'], color='teal', label='Loss')
axes[1].plot(hist.history['val_loss'], color='orange', label='Validation Loss')
axes[1].set_title('Loss')
axes[1].set_ylabel('Loss')
axes[1].set_xlabel('Epoch')
axes[1].set_xlim([0, 30])
axes[1].legend()

plt.tight_layout()  # Adjust layout to prevent overlapping
plt.show()

precision = Precision()
recall = Recall()
accuracy = BinaryAccuracy()

precision.reset_states()
recall.reset_states()
accuracy.reset_states()

for batch in test.as_numpy_iterator():
    X, y = batch
    yhat = model.predict(X)
    precision.update_state(y, yhat)
    recall.update_state(y, yhat)
    accuracy.update_state(y, yhat)

print(f'Precision: {precision.result()}, Recall: {recall.result()}, Accuracy: {accuracy.result()}')
