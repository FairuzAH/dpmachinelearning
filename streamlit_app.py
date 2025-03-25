import streamlit as st
import pandas as pd

st.title('Machine Learning App')

st.write('This is a Machine Learning Application')

with st.expander('Data'):
  st.write('**Raw data**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')
  df

  st.write('**X**')
  x_raw = df.drop('species', axis=1)
  x_raw

  st.write('**Y**')
  y_raw = df.species
  y_raw

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
  sex = st.selectbox('Ses',{'Male','Female' })

  #create a datafreame for the input features
  data = {'island': island,
          'bill_length_mm': bill_length_mm,
          'bill_depth_mm': bill_depth_mm,
          'flipper_length_mm': flipper_length_mm,
          'body_mass_g': body_mass_g,
          'sex': sex}
  input_df = pd.DataFrame(data, index=[0])
  input_penguins = pd.concat([input_df, x_raw ], axis=0)

# encode x(s)
encode = ['island', ' gender']
df_penguins = pd.get_dummies(input_penguins, prefix=encode)
input_row= df_penguins[:1]

# encode y
target_mapper = {'Adelie': 0,
                'Chinstrap':1,
                "Gentoo":2}
def target_encode[val]:
  return target_mapper[val]

with st.expander('Input features'):
  st.write('**Input Penguin**')
  input_df
  st.write('**Combined penguins data**')
  input_penguins
  st.write('**Encoded input penguin**')
  input_row


