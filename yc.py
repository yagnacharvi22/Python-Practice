import streamlit as st
st.title("Welcome to Streamlit")
username=st.text_input("Enter Username")
password=st.text_input("Enter Password")
if st.button("Login"):
     if username=="admin":
           if password=="1234":
                 st.success("Valid User")
           else:
                 st.error("Invalid Password")
     else:
            st.error("Invalid Username")