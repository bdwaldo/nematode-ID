#https://medium.com/geekculture/image-classifier-with-streamlit-887fc186f60

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
#for google sheet import
import gdown


#web page text
st.header("Plant-Parasitic Nematode Image Classification")
st.markdown("System under development by researchers")
st.caption("Questions may be directed to Benjamin.Waldo@usda.gov")

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
#model = tf.keras.models.load_model('nema_model.h5') #switch from load_model()


#bring in .h5 model from google drive
#https://pub.towardsai.net/how-to-deploy-models-larger-than-100mb-on-streamlit-1a553cc8bf0f
@st.cache_resource
def load_rf_model():
    url = 'https://drive.google.com/file/d/1Afnum9kXWdi8yD0ENfhTDmevyMRQ2osz/view?usp=drive_link'
    output_path = 'nema_model.h5'
    gdown.download(url, output_path, quiet=False, fuzzy=True)
    model = tf.keras.models.load_model('nema_model.h5')
    return model



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
  #predictions = model.predict(img_array)
  predictions = model.load_rf_model(img_array)  
  score = tf.nn.softmax(predictions[0])

  #print image can omit these three lines
  iu= Image.open(upload)
  c1.header('Input Image')
  c1.image(iu)
  
  #print prediction and probability
  st.write(
    "This image is most likely {} with a {:.2f} percent confidence."
    .format(class_names[np.argmax(score)], 100 * np.max(score)))

  
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





