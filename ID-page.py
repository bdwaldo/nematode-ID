#https://medium.com/geekculture/image-classifier-with-streamlit-887fc186f60

#import streamlit as st
#import numpy as np
#import PIL 
#import cv2
#import tensorflow
#from PIL import Image

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

#webpage text headers
#st.markdown('<h1 style="color:black;">Image classification model</h1>', unsafe_allow_html=False)
#st.markdown('<h2 style="color:gray;">The image classification model classifies nematodes into following categories:</h2>', unsafe_allow_html=False)
#st.markdown('<h3 style="color:gray;"> Hoplolaimus,  Mesocriconema, Pratylenchus</h3>', unsafe_allow_html=False)

st.header("Plant-Parasitic Nematode Image Classification")
st.markdown("Upload nematode image for identification")
st.caption("Model under development by UMD and USDA researchers")

#https://medium.com/geekculture/image-classifier-with-streamlit-887fc186f60
#pre-processing image
#adding text to web page to upload image


img_height = 180
img_width = 180

class_names = ['Hoplolaimus', 'Mesocriconema', 'Pratylenchus'] 


upload= st.file_uploader('Select image for identification', type=['png','jpg'])
c1, c2= st.columns(2)
model = tf.keras.models.load_model('nema_model.h5') #switch from load_model()

if upload is not None:
  #img = tf.keras.utils.load_img(
  # im, target_size=(img_height, img_width))
  image = keras.utils.load_img(upload, target_size=(img_height, img_width))
  #input_arr = img_to_array(image)
  #img = image.load_img(upload, target_size=(img_height, img_width)) #https://github.com/streamlit/streamlit/issues/4101
  #img_array = img_to_array(image) #https://keras.io/api/data_loading/image/

  #works
  img_array = np.array(image)

  #can unblock these two lines and it kinda works
  img_array = np.expand_dims(image,axis = 0)
  #img_array = tf.expand_dims(img_array, 0)
 
  predictions = model.predict(img_array)
  score = tf.nn.softmax(predictions[0])
  c1.write(predictions)
  c1.write(class_names[np.argmax(score)])
  
  #st.write(
    #"This image is most likely {} with a {:.2f} percent confidence."
    #.format(class_names[np.argmax(score)], 100 * np.max(score)))

  #https://stackoverflow.com/questions/38971293/get-class-labels-from-keras-functional-model
  #y_classes = predictions.argmax(axis = -1)
  
  
  
  #print(
   # "This image is most likely {} with a {:.2f} percent confidence."
   # .format(class_names[np.argmax(score)], 100 * np.max(score)))

  #st.write(model.predict(img, verbose=0)[0][0])
  
  
  
  #im= Image.open(upload)
  #img= np.asarray(im)
  #image= cv2.resize(img,(180, 180))
  #img= preprocess_input(image)
  #img= np.expand_dims(img, 0)
  
  #ii = tf.keras.utils.load_img(
  #  im, target_size=(img_height, img_width))
  #img_array = tf.keras.utils.img_to_array(ii)
  #img_array = tf.expand_dims(img_array, 0) # Create a batch
  #predictions = model.predict(img_array)
  #score = tf.nn.softmax(predictions[0])
  #c1.header('Input Image')
  #c1.image(im)
  #c1.write("This image most likely belongs to {} with a {:.2f} percent confidence."
  #         .format(class_names[np.argmax(score)], 100 * np.max(score)))
    
  

##########################
#https://www.tensorflow.org/tutorials/images/classification
#Predict image
# load the model we saved
#https://www.tensorflow.org/tutorials/keras/save_and_load
#model = tf.keras.models.load_model('nema_model.h5') #switch from load_model()





