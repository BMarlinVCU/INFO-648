import streamlit as st
import pickle

with open("lesson_10_streamlit_app/iris_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Lesson 25 App")

if st.button("Predict"):
    st.write("Model loaded!")
