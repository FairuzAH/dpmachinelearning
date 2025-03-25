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
#"species","island","bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g","sex"
  st.scatter_chart(data=df, x= 'bill_length_mm', y='body_mass_g', color='species')  
