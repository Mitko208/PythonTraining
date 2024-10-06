import cv2
import tensorflow as tf
import os
print("TensorFlow version:", tf.__version__)
print(os.getcwd())
#Load image
image = cv2.imread('./c10afe7519.jpg')
print(image.shape)

#Reshape image


#Load model
model = tf.keras.models.load_model('../../project 1/Homework/Snakes/Homework - Photo Recognition Teachable Machine/converted_keras/keras_model.h5')