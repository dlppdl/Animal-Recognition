#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 22:28:13 2019

@author: dlppdl
"""

#Importing the necessary modules
import cv2
import numpy as np
from keras.models import load_model

img_size = 200
model = load_model('./model/ars_cnn_model.h5')

animal = {
            0 : 'cat',
            1 : 'dog',
            2 : 'monkey',
            3 : 'cow',
            4 : 'elephant',
            5 : 'horse' ,
            6 : 'squirrel',
            7 : 'chicken' ,
            8 : 'spider' ,
            9 : 'sheep'
         }

def animalrecognition(path):

    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (int(img_size),int(img_size)))
    img = img.reshape(-1, img_size, img_size , 1).astype('float32')
    img /= 255 
    x = model.recognize(img)
    y = x > 0.5 # image must match more than 50% with any of the 10 animals 
    if y.any():  
        x = np.argmax(x,axis = 1)
        recognize_animal = animal[x[0]]
    else:
        recognize_animal = "Not Found"
        
    return  recognize_animal