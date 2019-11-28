import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
import pickle

dense_layers = [0]
layer_sizes = [64]
conv_lavers = [3]
X = pickle.load(open("X.pickle", "rb"))
y = pickle.load(open("Y.pickle", "rb"))
X = X/255.0

for dense_layer in dense_layers:
  for layer_size in layer_sizes:
    for conv_laver in conv_lavers:
      model = Sequential()
      model.add(Conv2D(layer_size, (3,3), input_shape = X.shape[1:]))
      model.add(Activation("relu"))
      model.add(MaxPooling2D(pool_size = (2,2)))
      
      
      for l in range(conv_laver-1):
        model.add(Conv2D(layer_size, (3,3)))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size = (2,2)))

      model.add(Flatten())
      
      for l in range(dense_layer-1):
        model.add(Dense(layer_size))
        model.add(Activation("relu"))

      model.add(Dense(1))
      model.add(Activation("sigmoid"))


      model.compile(loss="binary_crossentropy",
                   optimizer="adam",
                   metrics=['accuracy'])

      model.fit(X, y, batch_size = 32, epochs=10 , validation_split=0.1)
      
model.save("model")