import streamlit as st

name = st.text_input("full name")
age = st.number_input("age",min_value=0,max_value=120,value=25)
butn = st.button("click here")
if butn:
    if age < 12:
        st.text("age is less than the required age")
    else:
        st.text(name)
        st.text(age)   
                
