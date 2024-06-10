import tensorflow as tf
from tensorflow.keras import datasets, layers, models, utils
from tensorflow.keras.optimizers import Adam
from sklearn.utils import shuffle
import matplotlib.pyplot as plt
import numpy as np
from keras.preprocessing import image
import tensorflow.keras.backend as K


(x_train, y_train), (x_test,y_test) = datasets.cifar10.load_data()
y_train = y_train.reshape(-1,)
y_test = y_test.reshape(-1,)
classes = [""] #put in the different classes
x_train = tf.keras.utils.normalize(x_train)
x_test = tf.keras.utils.normalize(x_test)


cnn = models.Sequential([
    layers.Conv2D(filters=64, kernel_size=(3, 3), activation='relu', input_shape=(32, 32, 3)),
    layers.MaxPooling2D((2, 2)),
    
    
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])

cnn.compile(optimizer=Adam(learning_rate=0.0001),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

print("\nThe is the model plot: \n")
tf.keras.utils.plot_model(cnn, to_file='./trial1.png', show_shapes=True)
print("\n")
print("\nThe is the history for 5 epochs: \n")
cnn.fit(x_train, y_train, epochs=5)
print("\n")
print("\nThis is the evaluation.")
cnn.evaluate(x_test,y_test)