import streamlit as st
import pickle
import numpy as np


with open("models/crop_recommendation.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="Crop Recommender", layout="centered")

st.title("🌾 Smart Crop Recommendation System")

st.markdown("Provide the environmental and soil details below to get a recommended crop.")

# Example inputs
examples = {
    "Example 1": [90, 42, 43, 23.0, 82.0, 6.5, 220.0, 42.0],    # Maize
    "Example 2": [105, 40, 60, 29.5, 90.0, 5.8, 250.0, 70.0],   # Rice
    "Example 3": [80, 35, 50, 22.0, 65.0, 6.0, 300.0, 45.0],    # Coffee
    "Example 4": [120, 60, 80, 30.0, 85.0, 6.0, 280.0, 60.0],   # Banana
    "Example 5": [25, 15, 20, 20.0, 55.0, 6.2, 150.0, 35.0],    # Potato
}

selected_example = st.selectbox("Select an example input", ["Custom input"] + list(examples.keys()))

if selected_example != "Custom input":
    nitrogen, phosphorous, potassium, temperature, humidity, ph, rainfall, soil_moisture = examples[selected_example]
else:
    nitrogen = st.number_input("Ratio of Nitrogen (N)", min_value=0.0, step=0.1)
    phosphorous = st.number_input("Ratio of Phosphorous (P)", min_value=0.0, step=0.1)
    potassium = st.number_input("Ratio of Potassium (K)", min_value=0.0, step=0.1)
    temperature = st.number_input("Temperature (°C)", step=0.1)
    humidity = st.number_input("Humidity (%)", step=0.1)
    ph = st.number_input("Soil pH", min_value=0.0, max_value=14.0, step=0.1)
    rainfall = st.number_input("Rainfall (mm)", step=0.1)
    soil_moisture = st.number_input("Soil Moisture (%)", min_value=30.0, max_value=45.0, step=0.1)

    if soil_moisture < 30.0 or soil_moisture > 45.0:
        st.warning("⚠️ Soil Moisture value is outside the typical range (30-45%).")

if st.button("Recommend Crop"):
    features = np.array([[nitrogen, phosphorous, potassium, temperature, humidity, ph, rainfall, soil_moisture]])
    prediction = model.predict(features)
    st.success(f"✅ Recommended Crop: **{prediction[0]}**")
