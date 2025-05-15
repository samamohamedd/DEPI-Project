import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image
from tensorflow.keras.models import load_model

# تحميل النموذج
model = load_model("models/plant_disease_model.h5", compile=False)


output_layer = model.layers[-1]
print("Output layer name:", output_layer.name)
print("Number of classes:", output_layer.units)


# UI
st.header("🦠 Plant Disease Detection")

uploaded_file = st.file_uploader("Upload a plant leaf image", type=["jpg", "jpeg", "png"])

if uploaded_file:
   
    img = Image.open(uploaded_file).resize((224, 224))
    st.image(img, caption="Uploaded Image", use_container_width=True)
    
    img_array = np.expand_dims(np.array(img) / 255.0, axis=0)
    
    preds = model.predict(img_array)
   
    st.write("Prediction shape:", preds.shape)

    class_idx = np.argmax(preds)
    confidence = np.max(preds) * 100

    st.success(f"🦠 Detected class index: **{class_idx}** ({confidence:.2f}%)")
