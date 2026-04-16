import streamlit as st
import pickle

with open("iris_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Lesson 25 App")

if st.button("Predicbt"):
    st.write("Model loaded!")
