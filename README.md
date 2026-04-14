# 💻 Laptop-price-prediction-app

📌 Overview

This project is an end-to-end machine learning application that predicts laptop prices based on hardware and software specifications. It demonstrates the complete pipeline from data preprocessing and feature engineering to model training and deployment using Streamlit.


🧠 Problem Statement

Laptop prices vary significantly depending on specifications like RAM, CPU, GPU, and storage. This project aims to:

Predict laptop prices accurately

Help users understand how features affect price

Demonstrate real-world regression modeling

⚙️ Tech Stack

1.Python

2.Pandas & NumPy

3.Scikit-learn

4.Streamlit

5.Joblib

🔍 Features

✔ Interactive UI using Streamlit

✔ Real-time price prediction

✔ Handles categorical + numerical inputs

✔ Feature-engineered inputs (CPU type, OS grouping, etc.)

✔ Log-transformed model output for better accuracy


📊 Input Features

The model uses the following features:

-Company (Brand)

-Laptop Type

-Screen Size (Inches)

-RAM

-Weight

-Touchscreen & IPS Display

-Screen Resolution (x_res, y_res)

-CPU Type

-GPU Brand

-Operating System

-HDD & SSD Storage

🧪 How It Works

1.User selects laptop specifications from sidebar

2.Inputs are converted into structured format

3.Data is passed to trained ML model

4.Model predicts log(price)

5.Final price is calculated using exponential transformation

Output is displayed instantly

🎯 Key Highlights

-Built a complete ML pipeline from raw data to deployment

-Applied feature engineering techniques for better predictions

-Designed an interactive user interface

-Demonstrates real-world regression problem solving

🔮 Future Improvements

1.Add model explainability (SHAP values)

2.Improve UI/UX design

3.Deploy on cloud (Streamlit Cloud / Render)

4.Add price range classification
