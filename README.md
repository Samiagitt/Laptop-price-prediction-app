# 💻 2. LAPTOP PRICE PREDICTION

```markdown
# Laptop Price Prediction App

## Overview

This project is a machine learning-based web application that predicts laptop prices based on specifications such as brand, RAM, CPU, and storage. It demonstrates regression modeling and deployment using Streamlit.

---

## Objectives

- Predict laptop prices accurately  
- Understand how features impact pricing  
- Build an end-to-end regression system  

---

## Dataset

- Laptop dataset with specifications and prices  

---

## Data Processing Steps

- Feature engineering (CPU type, OS grouping)  
- Handling categorical variables  
- Log transformation of target variable  
- Data preprocessing and scaling  

---

## Model Details

- Model: Regression model  
- Target: Log-transformed price  
- Final output: Exponential transformation applied  

---

## Features Used

- Company  
- Laptop Type  
- Screen Size  
- RAM  
- Weight  
- Touchscreen & IPS  
- Resolution  
- CPU Type  
- GPU  
- Operating System  
- HDD & SSD  

---

## Application Features

- Interactive UI  
- Real-time price prediction  
- Handles categorical + numerical inputs  
- Displays predicted price  

---

## How It Works

User Input → Feature Processing → Model Prediction → Price Output  

---

## How to Run

```bash
git clone <repo-link>
cd laptop-price-app
pip install -r requirements.txt
streamlit run app.py
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
