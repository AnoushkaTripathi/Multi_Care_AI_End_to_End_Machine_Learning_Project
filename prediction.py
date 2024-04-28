# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

""

import numpy as np
import pickle


# loading the saved model
loaded_model = pickle.load(open('C:/Users/anous/Desktop/Multi_Care_AI/trained_model.sav', 'rb'))

    # changing the input_data to numpy array
input_data = (5,166,72,19,175,25.8,0.587,51)
input_data_as_numpy_array = np.asarray(input_data)


    # reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)





# creating a function for Prediction


    

     
    
  
    
    
    