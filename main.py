import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from sklearn.linear_model import LogisticRegression



st.title("Advertising ML Project")
ad_data = pd.read_csv('advertising.csv')
st.write(ad_data)
st.write("Cleaned Dataset")
ad_data.drop(['Ad Topic Line', 'City', 'Country', 'Timestamp'], axis=1, inplace=True)
st.write(ad_data)

st.sidebar.header('User Input Parameters')

def user_input_features():
    daily_time_spent = st.sidebar.slider('Daily_Time_Spent', 32, 91, 45)
    age = st.sidebar.slider('Age', 19, 61, 25)
    area_income = st.sidebar.slider('Area_Income', 13995, 79484, 50000)
    daily_internet_usage = st.sidebar.slider('Daily_internet_Usage', 104, 270, 45)
    male = st.sidebar.slider('Male', 0, 1, 0)

    data= {'Daily_Time_Spent': daily_time_spent,
           'Age': age,
           'Area_Income': area_income,
           'Daily_internet_Usage': daily_internet_usage,
           'Male': male}
    features = pd.DataFrame(data,index=[0])
    return features

df = user_input_features()

st.subheader('User Input Parameters')
st.write(df)

x = ad_data[['Daily Time Spent on Site', 'Age', 'Area Income', 'Daily Internet Usage', 'Male']]
y = ad_data['Clicked on Ad']

lm = LogisticRegression()
lm.fit(x,y)
prediction = lm.predict(df)
prediction_probability = lm.predict_proba(df)

st.subheader('Prediction')
st.write('Prediction = 0 means user not clicked on advertisement')
st.write('Prediction = 1 means user clicked on advertisement')
st.write(prediction)

st.subheader('Prediction_Probability')
st.write(prediction_probability)

