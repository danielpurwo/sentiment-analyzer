
import streamlit as st
import joblib

# Load model
model = joblib.load("sentiment_model.joblib")

st.title("📊 Sentiment Classifier Demo")
user_input = st.text_area("Enter a review:")
if st.button("Analyze"):
    prediction = model.predict([user_input])[0]
    st.write(f"Predicted Sentiment: **{prediction}**")
