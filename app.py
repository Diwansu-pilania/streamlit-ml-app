import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load the trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Load dataset to get feature names
df = pd.read_csv("data.csv", encoding="latin1")  # Adjust encoding if needed
feature_names = df.columns.drop('no2')  # Exclude target column

st.title("🌍 NO₂ Level Prediction App")

st.write("Enter the required values to predict NO₂ levels in air quality.")

# Create input fields for all features dynamically
user_input = []
for feature in feature_names:
    value = st.number_input(f"Enter {feature}", value=0.0)
    user_input.append(value)

# Convert input to NumPy array
user_input = np.array([user_input]).reshape(1, -1)

# Predict NO₂ levels
if st.button("Predict NO₂ Level"):
    prediction = model.predict(user_input)[0]
    st.success(f"Predicted NO₂ Level: {prediction:.2f}")
