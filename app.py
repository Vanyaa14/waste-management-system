import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load model
# ⚠️ Make sure to download waste_model.h5 and place it in this folder before running
model = tf.keras.models.load_model("waste_model.h5")

classes = ['Hazardous', 'Non-Recyclable', 'Organic', 'Recyclable']

def predict(img):
    img = img.resize((150,150))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)
    pred = model.predict(img)
    return classes[np.argmax(pred)]

# UI
st.title("Smart Waste Management System 🌱")
st.markdown("### ♻️ Upload an image to classify waste and get smart disposal guidance")
st.set_page_config(page_title="Waste Management", page_icon="♻️")
st.sidebar.markdown("## 🌱 Smart Waste Management")

st.sidebar.markdown("---")

st.sidebar.markdown("### 👩‍💻 About Project")
st.sidebar.write(
    "This AI-based system classifies waste into categories like Hazardous, Organic, Recyclable, and Non-Recyclable to promote proper disposal and environmental awareness."
)

st.sidebar.markdown("---")

st.sidebar.markdown("### 👤 Developed By")
st.sidebar.write("**Vanya Singh**")

st.sidebar.markdown("---")

st.sidebar.markdown("### 🌍 Why It Matters")
st.sidebar.write(
    "Proper waste segregation helps reduce pollution, conserve resources, and build a cleaner future."
)

st.sidebar.markdown("---")

st.sidebar.success("♻️ Think Green, Live Clean!")
st.markdown("---")
st.subheader("Why Waste Segregation Matters 🌍")
st.write("Proper waste segregation helps reduce pollution, saves resources, and protects the environment.")

uploaded_file = st.file_uploader("Upload waste image", type=["jpg","png","jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Uploaded Image")

    result = predict(img)

    st.subheader(f"Prediction: {result}")

    if result == "Organic":
        st.success("Dispose in compost/wet waste bin 🌱")
    elif result == "Recyclable":
        st.info("Send to recycling center ♻️")
    elif result == "Non-Recyclable":
        st.warning("Dispose in landfill waste 🚫")
    else:
        st.error("Handle carefully - hazardous waste ☠️")
