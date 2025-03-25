import streamlit as st
import panda as pd

st.title('Machine Learning App')

st.write('This is a Machine Learning Application')

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')
df
