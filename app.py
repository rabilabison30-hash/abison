import streamlit as st
import joblib
import numpy as np

model = joblib.load("model.pkl")

st.title("Prediksi Diabetes (RANDOM FOREST)")

preg = st.number_input("Pregnancies")
glu = st.number_input("Glucose")
bp = st.number_input("Blood Pressure")
skin = st.number_input("Skin Thickness")
ins = st.number_input("Insulin")
bmi = st.number_input("BMI")
dpf = st.number_input("Diabetes Pedigree Function")
age = st.number_input("Age")

if st.button("Prediksi"):

    data = np.array([[preg, glu, bp, skin, ins, bmi, dpf, age]])

    hasil = model.predict(data)

    st.success(f"Hasil Prediksi: {hasil[0]}")
     