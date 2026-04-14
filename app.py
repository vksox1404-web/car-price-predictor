import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

# Page config
st.set_page_config(page_title="Car Price AI", page_icon="🚗", layout="centered")

# Sidebar
st.sidebar.title("🚗 AI Car Price Predictor")
st.sidebar.info("Built with Machine Learning + Streamlit")

# Title
st.title("🚗 Car Price Predictor")
st.write("Predict car price instantly using AI model")

st.divider()

# INPUT MODE
st.subheader("💰 Car Price Input")

present_price = st.number_input(
    "Enter Car Price (QAR)",
    min_value=0,
    step=100,
    value=30000
)

# nice display only (no confusion)
st.markdown(f"""
### 💰 You entered:
**QAR {present_price:,.0f}**
""")

st.divider()

# Other inputs
kms_driven = st.number_input(
    "KMs Driven",
    min_value=0,
    step=500,
    value=30000
)

st.caption(f"📍 You entered: {kms_driven:,} km")

owner = st.selectbox("Owner", [0, 1, 2, 3])
age = st.slider("Car Age", 0, 30, 5)

fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel"])
seller = st.selectbox("Seller Type", ["Dealer", "Individual"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])

st.divider()

# Build input dataframe
input_data = pd.DataFrame(0, index=[0], columns=columns)

input_data["Present_Price"] = present_price
input_data["Kms_Driven"] = kms_driven
input_data["Owner"] = owner
input_data["Age"] = age

input_data["Fuel_Type_Diesel"] = 1 if fuel == "Diesel" else 0
input_data["Fuel_Type_Petrol"] = 1 if fuel == "Petrol" else 0

input_data["Seller_Type_Individual"] = 1 if seller == "Individual" else 0
input_data["Transmission_Manual"] = 1 if transmission == "Manual" else 0

# Predict button
if st.button("🔮 Predict Price"):
    prediction = model.predict(input_data)[0]

    st.success(f"💰 Estimated Selling Price: QAR {prediction * 1000:,.0f}")

    st.info("📊 AI Prediction based on trained dataset")

