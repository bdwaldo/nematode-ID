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
#import tensorflow as tf
import matplotlib.pyplot as plt
import cv2

#webpage text headers
#st.markdown('<h1 style="color:black;">Image classification model</h1>', unsafe_allow_html=False)
#st.markdown('<h2 style="color:gray;">The image classification model classifies nematodes into following categories:</h2>', unsafe_allow_html=False)
#st.markdown('<h3 style="color:gray;"> Hoplolaimus,  Mesocriconema, Pratylenchus</h3>', unsafe_allow_html=False)

st.header("Plant-Parasitic Nematode Image Classification")
st.markdown("Upload nematode image for identification")
st.caption("Developed by UMD and USDA researchers")


#pre-processing image
#adding text to web page to upload image
upload= st.file_uploader('Select image for identification', type=['png','jpg'])
c1, c2= st.columns(2)
if upload is not None:
  im= Image.open(upload)
  img= np.asarray(im)
  image= cv2.resize(img,(224, 224))
  img= preprocess_input(image)
  img= np.expand_dims(img, 0)
  c1.header('Input Image')
  c1.image(im)
  c1.write(img.shape)

##########################
#https://www.tensorflow.org/tutorials/images/classification
#Predict image
#load image
img = tf.keras.utils.load_img(
    '/90daydata/nematode_ml/test/H_columbus_G-12013_10x_1.png', target_size=(img_height, img_width)
)
# load the model we saved
model = load_model('nema_model.h5')

img_array = tf.keras.utils.img_to_array(img)
img_array = tf.expand_dims(img_array, 0) # Create a batch

predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])

print(
    "This image most likely belongs to {} with a {:.2f} percent confidence."
    .format(class_names[np.argmax(score)], 100 * np.max(score)))


