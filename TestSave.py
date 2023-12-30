from matplotlib import pyplot as plt
from tensorflow.keras.metrics import Precision, Recall, BinaryAccuracy
import os

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

for batch in test.as_numpy_iterator():
    X, y = batch
    yhat = model.predict(X)
    precision.update_state(y, yhat)
    recall.update_state(y, yhat)
    accuracy.update_state(y, yhat)

print(f'Precision: {precision.result()}, Recall: {recall.result()}, Accuracy: {accuracy.result()}')

#saving model
model.save(os.path.join('models','ScientificVSArt.h5'))
