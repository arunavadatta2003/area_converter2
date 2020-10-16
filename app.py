# Import the libraries
import streamlit as st
import pandas as pd

# Add a title and an image
st.write("""
# Area Converter Web Application 2
created by **Arunava Datta**
""")

# Set the Background and sidebar
st.markdown("""
<style>
body {
    background-color: #315168;
    color: white;
}
sidebar.sidebar-content {
    background-color: #46484a;
    color: white;
}
</style>
    """, unsafe_allow_html=True)

# Create a function to get user inputs
st.header('User Input')
x = st.number_input("Bigha",0.0)
y = st.number_input("Katha",0.0)
z = st.number_input("Chattak",0.0,15.9999)
sq_ft = st.number_input("Sq.ft.",0.0,44.9999)

total_sq_ft = round(x*20*720 + y*720 + z*45 + sq_ft,2)
st.write("Total Sq.ft. - ", total_sq_ft)

total_sq_m = round(total_sq_ft/10.764,2)
st.write("Total Sq.m. - ", total_sq_m)

if total_sq_m <=200:
    a = 65
elif total_sq_m >= 500:
    a = 50
elif 200 < total_sq_m < 500:
    a = round(50 + (0.05*(500 - total_sq_m)),2)
st.write('Permissible Ground Coverage -',a,"%")






