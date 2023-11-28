#installing the pakages
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
#first line
st.write('Hello world')
option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))
x= Range(1,30)
y=Range(1,30)
plt.scatter(x,y)