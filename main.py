import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import  LabelEncoder
import xgboost as xgb
import numpy as np
import joblib
st.header("Resume Parser App")
uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")



# load model
model = joblib.load('resume_parser.obj')
entities = model.predict(uploaded_file)

def hello(dic):
    res = ''
    for (k,v) in dic:
      res+= k+': '
      res+= ', '.join(list(v))
      res+='\n'
      
     return res
  
 st.write(hello(entities)

