#https://medium.com/geekculture/image-classifier-with-streamlit-887fc186f60

import streamlit as st
import tensorflow as tf

from tensorflow import keras

#webpage text headers
st.markdown('<h1 style="color:black;">Vgg 19 Image classification model</h1>', unsafe_allow_html=True)
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
st.set_option('deprecation.showfileUploaderEncoding', False)
@st.cache(allow_output_mutation=True)
def load_model():
    model=tf.keras.models.load_model('nema_model.h5')
    return model
with st.spinner('Model is being loaded..'):
    model=load_model()
