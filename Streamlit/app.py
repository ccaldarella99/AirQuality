from altair.vegalite.v4.schema.channels import Color
import streamlit as st
import plotly.express as px
import datetime
import numpy as np
import pandas as pd

import pickle



#image
from PIL import Image
img1 = Image.open("galogo.jpeg")
st.image(img1, width =200)


st.title( '"Welcome and Thank you for using our Air Quality Index Predictor Web App"')
st.subheader(" Developpers: ABC (Anna-Ben-Chris)")
#Date Input
import datetime
today = st.date_input('Today is', datetime.datetime.now())

month = today.month
weekday = today.weekday()


#Text title
#st.title('Air Quality Predictor Web App')

#Header/Subheader

st.header('What is the AQI (Air Quality Index)in Cleveland, Ohio? ')


#load data

df = pd.read_csv('clean_aqi.csv')
#df

show_df = st.checkbox("Click here to view the raw data")

if show_df:
    df


# Images
from PIL import Image
img = Image.open("airquality.jpeg")
st.image(img, width =600)





#load data

#get user input
# Slider

temp_level = st.slider("Input the Temperature (F)", -10,100)

CO_level = st.slider("Input the Carbon Monoxide Level", 0,10)

no2_level = st.slider("Input the Nitrogen Dioxide Level", 0,50)

pm10_level= st.slider("Input the pm10 Level", 0,100)

pm2_5_level = st.slider("Input the pm2.5 Level", 0,100)

#with open('baseline_model1.pkl', 'rb') as f:
    #model = pickle.load(f)

#user_values = np.array([np.nan, np.nan, np.nan, CO_level, np.nan, no2_level, np.nan, o3_level, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, temp_level, month, weekday])
#prediction = model.predict(user_values.reshape(1,-1))

#st.header(f'The predicted AQI is: {prediction[0]}')

with open('saved-aqi-basic-model.pkl', 'rb') as f:
    model = pickle.load(f)

user_values = np.array([ temp_level, CO_level, no2_level, pm10_level, pm2_5_level])
prediction = model.predict(user_values.reshape(1,-1))

show_prediction = round(prediction[0])

st.header(f'The predicted AQI is: {show_prediction}')


