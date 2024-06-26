#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#https://www.tensorflow.org/tutorials/images/classification


# In[1]:


#load libraries

import matplotlib.pyplot as plt
import numpy as np
import PIL
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential


# In[4]:


#set working direcory
import os
os.chdir('/90daydata/nematode_ml/nematode') 


# In[5]:


#print working directory
import os
cwd = os.getcwd()
print(cwd)


# In[8]:


#set working directory variable to match tutorial
import pathlib
data_dir = cwd
data_dir = pathlib.Path(data_dir).with_suffix('')


# In[9]:


#count number of images with .jpg extension
image_count = len(list(data_dir.glob('*/*.jpg')))
print(image_count)


# In[10]:


#look at first image in Hoploalimus
Hoplolaimus = list(data_dir.glob('Hoplolaimus/*'))
PIL.Image.open(str(Hoplolaimus[0]))


# In[11]:


#look at first image in Mesocriconema
Mesocriconema = list(data_dir.glob('Mesocriconema/*'))
PIL.Image.open(str(Mesocriconema[0]))


# In[12]:


#look at first image in Pratylenchus
Pratylenchus = list(data_dir.glob('Pratylenchus/*'))
PIL.Image.open(str(Pratylenchus[0]))


# In[14]:


#define some parameters for the loader
batch_size = 32
img_height = 180
img_width = 180


# In[15]:


#use 80% images for training
train_ds = tf.keras.utils.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  subset="training",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)


# In[16]:


#use 20% images for validatin
val_ds = tf.keras.utils.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  subset="validation",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)


# In[17]:


#print class names
class_names = train_ds.class_names
print(class_names)


# In[18]:


#show first 9 images in dataset
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 10))
for images, labels in train_ds.take(1):
  for i in range(9):
    ax = plt.subplot(3, 3, i + 1)
    plt.imshow(images[i].numpy().astype("uint8"))
    plt.title(class_names[labels[i]])
    plt.axis("off")


# In[19]:


#image batch shape is the # of images (32),
#with a shape of 180x180 with 3 color channels

#label batch is the tensor shape (32, ) 
#indicating 32 labels corresponindg to 32 images
#call .numpy() on the image_batch and labesl_batch tensors to 
#convert them to a numpy.ndarray

for image_batch, labels_batch in train_ds:
  print(image_batch.shape)
  print(labels_batch.shape)
  break


# In[20]:


#Dataset.cache keeps images in memory 
#after they're loaded off disk during the first epoch
#this ensures dataset will not become a bottleneck while training the model
#helps with performance of large datasets

#dataset.prefetch overlaps data preprocessing and model execution while training
#https://www.tensorflow.org/guide/data_performance

AUTOTUNE = tf.data.AUTOTUNE

train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)


# In[21]:


#standardize the images
#[0,255] RBG values are large and do not work well for CNN, make small
#here we are standardizing the values in the [0,1] range
normalization_layer = layers.Rescaling(1./255)


# In[22]:


#calling Dataset.map

normalized_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))
image_batch, labels_batch = next(iter(normalized_ds))
first_image = image_batch[0]
# Notice the pixel values are now in `[0,1]`.
print(np.min(first_image), np.max(first_image))


# In[ ]:


#Create model


# In[23]:


#This Keras model consists of 3 convolutional blocks (tf.keras.layers.Conv2D)
#with a max pooling layer (tf.keras.layers.MaxPooling2D) for each block
#a fully connected layer (tf.keras.layers.Dense)
#128 units on top of the fully connected layer that is activated by a ReLu function ('relu')

#not tuned for high accuracy

num_classes = len(class_names)

model = Sequential([
  layers.Rescaling(1./255, input_shape=(img_height, img_width, 3)),
  layers.Conv2D(16, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(32, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(64, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Flatten(),
  layers.Dense(128, activation='relu'),
  layers.Dense(num_classes)
])


# In[24]:


#Compile the model

# The tf.keras.optimizers.Adam optimizer and
# tf.keras.losses.SparseCategoricalCrossentropy loss function
# were selected for this tutorial
# pass 'metrics' to 'Model.compile' to find training 
#and validation accuracy for each trainng epoch

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])


# In[32]:


#print model summary
model.summary()


# In[25]:


#Train model with 10 epochs
#with the  'Model.fit' method
epochs=10
history = model.fit(
  train_ds,
  validation_data=val_ds,
  epochs=epochs
)


# In[26]:


#create plots to visulaize loss and accuracy 
#on training and validation sets

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(epochs)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()


# In[ ]:


# there are addtional steps in the tutorial to
#improve accuracy. For this example, 
#I simply want to create a basic model


# In[35]:


#Save model
#https://www.tensorflow.org/tutorials/keras/save_and_load


# In[30]:


# Save the entire model as a `.keras` zip archive.
model.save('nema_model.keras')


# In[31]:


#Reload a fresh Keras model from the '.keras' zip file

new_model = tf.keras.models.load_model('nema_model.keras')

# Show the model architecture
new_model.summary()


# In[33]:


#show location of model
import pathlib
pathlib.Path('nema_model.keras').parent.resolve()


# In[ ]:




