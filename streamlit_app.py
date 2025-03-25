import streamlit as st
import pandas as pd

st.title('Machine Learning App')

st.write('This is a Machine Learning Application')

with st.expander('Data'):
  st.write('**Raw data**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')
  df

  st.write('**X**')
  X = df.drop('species', axis=1)
  X

  st.write('**Y**')
  X = df.species
  X

with st.expander('Data visualization'):
  st.scatter_chart(data=df, x= 'bill_length_mm', y='body_mass_g', color='species')  
#Data preparations
with st.sidebar:
  st.header('Input Features')
  #"species","island","bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g","sex"
  island = st.selectbox('Island',{'Biscoe','Dream', 'Togerseon' })
  bill_length_mm = st.slider('Bill length (mm)', 32.1, 59.6, 43.9)
  bill_depth_mm = st.slider('Bill depth (mm)', 13.1, 21.5, 17.2)
  flipper_length_mm = st.slider('Flipper length (mm)', 172.0, 231.0, 201.0)
  body_mass_g = st.slider('Body mass in (g)', 2700,6300, 4200)
  gender = st.selectbox('Gender',{'Male','Female' })

  #create a datafreame for the input features
  data = {'island': island,
          'bill_length_mm': bill_length_mm,
          'bill_depth_mm': bill_depth_mm,
          'flipper_length_mm': flipper_length_mm,
          'body_mass_g': body_mass_g,
          'gender': gender}
  input_df = pd.Dataframe(data, index=[0])
  input_penguins = pd.concat([input_df, X ], axis=0)
  
input_penguins
          
          
