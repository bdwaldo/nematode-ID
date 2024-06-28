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

def predict(image):
    classifier_model = "nema_model.h5"
    IMAGE_SHAPE = (224, 224,3)
    model = load_model(classifier_model, compile=False, custom_objects={'KerasLayer': hub.KerasLayer})
    test_image = image
    test_image = preprocessing.image.img_to_array(test_image)
    test_image = test_image / 255.0
    test_image = np.expand_dims(test_image, axis=0)
    class_names = [
          'Hoplolaimus',
          'Mesocriconema',
          'Pratylenchus']
    predictions = model.predict(test_image)
    scores = tf.nn.softmax(predictions[0])
    scores = scores.numpy()
    results = {
          'Hoplolaimus': 0,
          'Mesocriconema': 0,
          'Pratylenchus': 0
    }
  print(predictions)



#result = f"{class_names[np.argmax(scores)]} with a { (100 * np.max(scores)).round(2) } % confidence." 
   # return result
