#importing modules
import numpy as np
import tensorflow
import tensorflow.keras as keras

#Loading dataset
mnist_fashion = keras.datasets.fashion_mnist
(training_images, training_labels), (test_images,test_labels) = mnist_fashion.load_data()

# Scaling and reshaping
test_images =test_images/255.0
# test_images = test_images.reshape((10000,28,28,1))

#Building layers of model
cnn_model = keras.models.Sequential()
cnn_model.add(keras.layers.Conv2D(50, (3, 3), activation='relu', input_shape=(28, 28, 1), name='Conv2D_layer'))  #
cnn_model.add(keras.layers.MaxPooling2D((2, 2), name='Maxpooling_2D'))
cnn_model.add(keras.layers.Flatten(name='Flatten'))
cnn_model.add(keras.layers.Dense(50, activation='relu',name='Hidden_layer'))
cnn_model.add(keras.layers.Dense(10, activation='softmax',name='Output_layer'))

# compiling
cnn_model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# loading the weights
cnn_model.load_weights("cnn_model.h5")

# Predict
print("Predict the digit in the first 10 images in the test dataset")
y_pred = cnn_model.predict(test_images[:10])
print("Predicted image label:", np.argmax(y_pred,1))
print("Ground-truth image label:", test_labels[:10])
