import streamlit as st
import pandas as pd
import joblib
import numpy as np

# ----------------------------
# Load Model
# ----------------------------
model_path = r"E:\Project2-LaptopPricePrediction\laptop_price_model.pkl"

try:
    model = joblib.load(model_path)
except FileNotFoundError:
    st.error(f"Model file not found at {model_path}. Make sure it exists!")
    st.stop()

# ----------------------------
# App Title
# ----------------------------
st.set_page_config(page_title="Laptop Price Predictor", page_icon="💻", layout="centered")
st.title("💻 Laptop Price Prediction App")
st.write("Predict the price of a laptop based on its specifications.")

# ----------------------------
# Sidebar for Inputs
# ----------------------------
st.sidebar.header("Select Laptop Features")

# ✅ Company (from dataset)
company = st.sidebar.selectbox(
    "Brand (Company)",
    ["Acer","Apple","Asus","Chuwi","Dell","Fujitsu","Google","HP","Huawei","LG",
     "Lenovo","MSI","Mediacom","Microsoft","Razer","Samsung","Toshiba","Vero","Xiaomi"]
)

# ✅ TypeName (must match training exactly)
type_name = st.sidebar.selectbox(
    "Laptop Type (TypeName)",
    ["Notebook", "Ultrabook", "Gaming", "2 in 1 Convertible", "Netbook", "Workstation"]
)

# Numeric
inches = st.sidebar.slider("Screen Size (Inches)", 10.0, 18.0, 15.6)
ram = st.sidebar.slider("RAM (GB) (Ram)", 2, 64, 8)
weight = st.sidebar.slider("Weight (kg) (Weight)", 0.8, 5.0, 2.5)

# Engineered flags (already engineered in training)
touch = st.sidebar.selectbox("TouchScreen", ["No", "Yes"])
touchscreen = 1 if touch == "Yes" else 0

ips = st.sidebar.selectbox("IPS Display", ["No", "Yes"])
ips_val = 1 if ips == "Yes" else 0

# ✅ Resolutions from dataset
x_res = st.sidebar.selectbox("Screen Width (x_res)", [1366,1440,1600,1920,2160,2256,2304,2400,2560,2736,2880,3200,3840])
y_res = st.sidebar.selectbox("Screen Height (y_res)", [768,900,1080,1200,1440,1504,1600,1800,1824,2160])

# ✅ cpu_type (EXACT categories from your feature engineering)
cpu_type = st.sidebar.selectbox(
    "Processor Category (cpu_type)",
    ["Intel Core i3", "Intel Core i5", "Intel Core i7", "Other Intel Processor", "AMD processor"]
)

# ✅ Gpu (brand only, EXACT)
gpu = st.sidebar.selectbox("GPU Brand (Gpu)", ["Intel", "AMD", "Nvidia"])

# ✅ OpSys (EXACT mapping result from your notebook)
op_sys = st.sidebar.selectbox(
    "Operating System (OpSys)",
    ["Windows", "Mac", "Linus/Android/No OS/Chrome OS"]
)

# Storage
hdd = st.sidebar.selectbox("HDD (GB) (HDD)", [0, 128, 256, 512, 1024, 2048])
ssd = st.sidebar.selectbox("SSD (GB) (SSD)", [0, 128, 256, 512, 1024, 2048])

# ----------------------------
# Predict Button
# ----------------------------
if st.button("Predict Price"):
    # ✅ Columns EXACTLY as training (x = df.drop(columns=['Price']))
    input_df = pd.DataFrame({
        "Company": [company],
        "TypeName": [type_name],
        "Inches": [float(inches)],
        "Ram": [int(ram)],
        "Gpu": [gpu],
        "OpSys": [op_sys],
        "Weight": [float(weight)],
        "TouchScreen": [int(touchscreen)],
        "IPS": [int(ips_val)],
        "x_res": [int(x_res)],
        "y_res": [int(y_res)],
        "cpu_type": [cpu_type],
        "HDD": [int(hdd)],
        "SSD": [int(ssd)]
    })

    st.write("### Input Features")
    st.dataframe(input_df)

    try:
        # ✅ Your model was trained on log(price)
        pred_log = float(model.predict(input_df)[0])
        pred_price = float(np.exp(pred_log))
        st.success(f"💰 Estimated Laptop Price: {pred_price:,.2f}")
        st.caption(f"(log-price output: {pred_log:.4f})")
    except Exception as e:
        st.error(f"Prediction failed. Check your input features.\n\nError: {e}")

# ----------------------------
# Footer
# ----------------------------
st.markdown("---")