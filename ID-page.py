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
import gdown #for google sheet import



#web page text
st.header("Plant-Parasitic Nematode Image Classification")
st.markdown("System under development by researchers")
st.caption("Questions may be directed to Benjamin.Waldo@usda.gov")

#https://medium.com/geekculture/image-classifier-with-streamlit-887fc186f60
#pre-processing image


#image dimensions
img_height = 180
img_width = 180


#These correspond to the directory names in alphabetical order.
#https://www.tensorflow.org/tutorials/images/classification
#https://stackoverflow.com/questions/38971293/get-class-labels-from-keras-functional-model
#class_names = ['Lance', 'Lesion', 'Ring', 'RKN', 'Spiral', 'Stubby', 'Stunt'] 
class_names = ['Lance', 'Lesion', 'Ring']

#adding text to web page to upload image
upload= st.file_uploader('Select image for identification', type=['png','jpg'])
c1, c2= st.columns(2)


###############################################
#unblock line below if model is in Github repository
#load .h5 model from github repository
#https://www.tensorflow.org/tutorials/keras/save_and_load

#model = tf.keras.models.load_model('nema_model.h5') #switch from load_model()
################################################

################################################
#block out lines below if pulling model file from github
#bring in .h5 model from google drive
#https://pub.towardsai.net/how-to-deploy-models-larger-than-100mb-on-streamlit-1a553cc8bf0f
@st.cache_resource
def load_rf_model():
    url = 'https://drive.google.com/file/d/1Afnum9kXWdi8yD0ENfhTDmevyMRQ2osz/view?usp=drive_link' #CHANGE URL
    output_path = 'nema_model.h5' #CHANGE FILENAME
    gdown.download(url, output_path, quiet=False, fuzzy=True)
    model = tf.keras.models.load_model('nema_model.h5') #CHANGE FILE NAME
    return model

model = tf.keras.models.load_model('nema_model.h5')
####################################################

#function for uploading image
#https://github.com/streamlit/streamlit/issues/4101
#https://keras.io/api/data_loading/image/

if upload is not None:
  #load image from upload button
  image = keras.utils.load_img(upload, target_size=(img_height, img_width))

  #convert image to array
  img_array = np.array(image).astype('float32')/255
  img_array = np.expand_dims(img_array,axis = 0)

  #make prediction from uploaded image
  predictions = model.predict(img_array)   
  class_index = np.argmax(predictions) # Get the index of the highest probability class
  predicted_class = class_names[class_index] # Map the index to the corresponding class name
  score = tf.nn.softmax(predictions[0]) #

  #print image can omit these three lines
  iu= Image.open(upload)
  c1.header('Input Image')
  c1.image(iu)
  
  #print prediction and probability
  #https://stackoverflow.com/questions/54167910/keras-how-to-use-argmax-for-predictions
  st.write(
    "This image is most likely {} with a {:.2f} percent confidence."
    .format(predicted_class, 100 * np.max(score)))



 


