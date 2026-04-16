import streamlit as st
import pickle
import pandas as pd

with open("lesson_10_streamlit_app/iris_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Lesson 25 App")
st.write("Enter flower measurements below.")

sepal_length = st.number_input("Sepal length", min_value=0.0, value=5.1)
sepal_width = st.number_input("Sepal width", min_value=0.0, value=3.5)
petal_length = st.number_input("Petal length", min_value=0.0, value=1.4)
petal_width = st.number_input("Petal width", min_value=0.0, value=0.2)

if st.button("Predict"):
    new_flower = pd.DataFrame([{
        "sepal length (cm)": sepal_length,
        "sepal width (cm)": sepal_width,
        "petal length (cm)": petal_length,
        "petal width (cm)": petal_width
    }])

    prediction = model.predict(new_flower)[0]

    class_names = {
        0: "Setosa",
        1: "Versicolor",
        2: "Virginica"
    }

    st.success(f"Prediction: {class_names[prediction]}")
