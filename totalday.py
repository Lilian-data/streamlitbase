# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 16:47:16 2023
@author: lilian
"""

import numpy as np
import altair as alt
import pandas as pd
import streamlit as st



st.header('DAY 03 st.button')

if st.button('say hello'):
     st.write('why hello?')
else:
     st.write('goodbye')



st.header("DAY 04 st.write c'est fantastique")

st.write("Hello, *World!* :sunglasses:")

st.write(1234)

df = pd.DataFrame({
    'premiere colonne' : [1,2,3,4],
    'deuxième colonne' : [10,20,30,40]
    })
st.write(df)

st.write('Ci dessous se trouve une Dataframe: ', df , 'Ci dessus se trouve une Dataframe.' )

df2= pd.DataFrame(
    np.random.randn(200 ,3 ),
    columns=['a' ,'b' ,'c'])

c = alt.Chart(df2).mark_circle().encode(
    x='a' ,y='b', color='c' ,tooltip=['a' ,'b' ,'c'])
st.write(c)