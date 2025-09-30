import streamlit as st
import pandas as pd 

st.title('Heart Disease app')
st.info('This is app for Heart disease predicition')
df=pd.read_csv('https://raw.githubusercontent.com/Keromedhat/Heart-Disease-app/refs/heads/master/cleaned%20Heart%20Disease%20.csv')
df
