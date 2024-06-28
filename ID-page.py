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
  #img= preprocess_input(image)
  img= np.expand_dims(img, 0)
  c1.header('Input Image')
  c1.image(im)
  c1.write(img.shape)

##########################
#Predict image
# load the model we saved
model = load_model('nema_model.h5')
model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

# predicting images
#img = image.load_img('test1.jpg', target_size=(img_width, img_height))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)

images = np.vstack([x])
classes = model.predict_classes(image)
print(classes)

# predicting multiple images at once
#img = image.load_img('test2.jpg', target_size=(img_width, img_height))
#y = image.img_to_array(img)
#y = np.expand_dims(y, axis=0)

# pass the list of multiple images np.vstack()
#images = np.vstack([x, y])
#classes = model.predict_classes(images, batch_size=10)

# print the classes, the images belong to
#print classes
#print classes[0]
#print classes[0][0]

