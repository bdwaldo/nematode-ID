#https://medium.com/geekculture/image-classifier-with-streamlit-887fc186f60
#this code runs on a simple .h5 model file
#depreciating to attempt to use pytorch trained model 


import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import cv2
from tensorflow import keras
from keras import models 
#from keras.preprocessing.image import img_to_array
from tensorflow.keras.utils import img_to_array
from tensorflow.keras.preprocessing import image

#web page text
st.header("Plant-Parasitic Nematode Image Classification")
st.markdown("System under development by researchers")
#st.caption("Questions may be directed to Benjamin.Waldo@usda.gov")

#https://medium.com/geekculture/image-classifier-with-streamlit-887fc186f60
#pre-processing image


#image dimensions
img_height = 180
img_width = 180

#names to ID. Need to figure out how to pull directly from .h5 file
#https://stackoverflow.com/questions/38971293/get-class-labels-from-keras-functional-model
class_names = ['Hoplolaimus', 'Mesocriconema', 'Pratylenchus'] 

#adding text to web page to upload image
upload= st.file_uploader('Select image for identification', type=['png','jpg'])
c1, c2= st.columns(2)

#load .h5 model from github repository
#https://www.tensorflow.org/tutorials/keras/save_and_load
model = tf.keras.models.load_model('nema_model.h5') #switch from load_model()

#function for uploading image
#https://github.com/streamlit/streamlit/issues/4101
#https://keras.io/api/data_loading/image/

if upload is not None:
  #load image from upload button
  image = keras.utils.load_img(upload, target_size=(img_height, img_width))

  #convert image to array
  img_array = np.array(image)
  img_array = np.expand_dims(img_array,axis = 0)

  #make prediction from uploaded image
  predictions = model.predict(img_array)
  score = tf.nn.softmax(predictions[0])

  #print image can omit these three lines
  iu= Image.open(upload)
  c1.header('Input Image')
  c1.image(iu)
  
  #print prediction and probability
  st.write(
    "This image is most likely {} with a {:.2f} percent confidence."
    .format(class_names[np.argmax(score)], 100 * np.max(score)))
