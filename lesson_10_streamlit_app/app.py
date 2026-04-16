import streamlit as st
import pickle

with open("your_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Lesson 10 App")

if st.button("Predict"):
    st.write("Model loaded!")
    
