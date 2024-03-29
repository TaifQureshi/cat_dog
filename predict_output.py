import cv2
import tensorflow as tf

category = ["Dog", "Cat"]

def prepare(filepath):
  img_size = 100
  img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
  new_array = cv2.resize(img_array, (img_size, img_size))
  return new_array.reshape(-1 , img_size, img_size, 1)

model = tf.keras.models.load_model("gdrive/My Drive/Data/model")

prediction = model.predict([prepare('gdrive/My Drive/Data/cat.jpg')])
print([int(prediction[0])])