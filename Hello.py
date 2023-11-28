#installing the pakages
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
#first line
st.write('Hello world')
option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)
option = st.selectbox(
    'What is your name ?',
    ('Email', 'Home phone', 'Mobile phonne'))

st.write('You selected:', option)
#plot
plt.plot(x,y)

st.pyplot