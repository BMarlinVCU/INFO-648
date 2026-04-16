import os
import pickle
import pandas as pd
import streamlit as st

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "RF_model.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

st.title("Random Forest Prediction App")
st.write("Enter the values below to generate a prediction.")

age = st.number_input("Age", min_value=0, max_value=100, value=35)
uhrsworkt = st.number_input("Usual Hours Worked per Week", min_value=0, max_value=100, value=40)
statefip = st.number_input("State FIPS", min_value=1, max_value=56, value=51)

sex = st.selectbox("Sex", options=["Male", "Female"])
education = st.selectbox(
    "Education",
    options=[
        "High school",
        "Some college",
        "Bachelor",
        "Master",
        "Doctorate"
    ]
)

if st.button("Predict"):
    new_data = pd.DataFrame([{
        "AGE": age,
        "UHRSWORKT": uhrsworkt,
        "STATEFIP": statefip,
        "SEX": sex,
        "education": education
    }])

    st.write("Input data:")
    st.dataframe(new_data)

    try:
        prediction = model.predict(new_data)[0]
        st.success(f"Prediction: {prediction}")

        if hasattr(model, "predict_proba"):
            probs = model.predict_proba(new_data)[0]
            st.write("Prediction probabilities:")
            st.write(probs)

    except Exception as e:
        st.error("Prediction failed.")
        st.code(str(e))
