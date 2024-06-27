#https://medium.com/geekculture/image-classifier-with-streamlit-887fc186f60



import streamlit as st
import numpy as np
import PIL 
import cv2

from PIL import Image

#webpage text headers
st.markdown('<h1 style="color:black;">Image classification model</h1>', unsafe_allow_html=True)
st.markdown('<h2 style="color:gray;">The image classification model classifies nematodes into following categories:</h2>', unsafe_allow_html=True)
st.markdown('<h3 style="color:gray;"> Hoplolaimus,  Mesocriconema, Pratylenchus</h3>', unsafe_allow_html=True)

#pre-processing image
#adding text to web page to upload image
upload= st.file_uploader('Insert image for classification', type=['png','jpg'])
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

  ############################
#load weights of the trained model.
  input_shape = (224, 224, 3)
  optim_1 = Adam(learning_rate=0.0001)
  n_classes=6
  vgg_model = model(input_shape, n_classes, optim_1, fine_tune=2)
  
  # prediction on model
  vgg_preds = vgg_model.predict(img)
  vgg_pred_classes = np.argmax(vgg_preds, axis=1)
  c2.header('Output')
  c2.subheader('Predicted class :')
  c2.write(classes[vgg_pred_classes[0]] )
