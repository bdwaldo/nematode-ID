import streamlit as st

st.markdown('<h1 style="color:black;">Vgg 19 Image classification model</h1>', unsafe_allow_html=True)
st.markdown('<h2 style="color:gray;">The image classification model classifies nematodes into following categories:</h2>', unsafe_allow_html=True)
st.markdown('<h3 style="color:gray;"> Hoplolaimus,  Mesocriconema, Pratylenchus</h3>', unsafe_allow_html=True)

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
