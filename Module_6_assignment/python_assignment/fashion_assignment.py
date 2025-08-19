import os
import tensorflow as tf
from keras.datasets import fashion_mnist
from keras import models, layers
import matplotlib.pyplot as plt
import numpy as np

save_dir = os.path.dirname(os.path.abspath(__file__))

(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

x_train = x_train / 255.0
x_test = x_test / 255.0

x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)

model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))

predictions = model.predict(x_test[:2])

class_names = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
               "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]

for i in range(2):
    pred_label = np.argmax(predictions[i])
    true_label = y_test[i]
    plt.imshow(x_test[i].reshape(28, 28), cmap='gray')
    plt.title(f"Predicted: {class_names[pred_label]}, True: {class_names[true_label]}")
    plt.axis('off')
    plt.savefig(os.path.join(save_dir, f"prediction_{i}.png"))
    plt.show()

model.save(os.path.join(save_dir, "fashion_cnn.h5"))
np.savetxt(os.path.join(save_dir, "predictions.txt"), predictions[:2])
