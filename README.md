# 🚗 Qatar Car Price Predictor

An end-to-end Machine Learning web application that predicts used car prices in the Gulf market. Built with Python and deployed with Streamlit.

---

## 🌐 Live Demo
👉 [Try the app here](https://vksox1404-web-car-price-predictor.streamlit.app)

---

## 📌 Project Overview

Most car price prediction projects are trained on Indian or Western datasets, making their predictions irrelevant to Gulf markets. This project solves that by using a real Gulf market dataset with prices in **Qatari Riyals (QAR)**.

---

## ⚙️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| pandas & NumPy | Data cleaning & processing |
| scikit-learn | Model training |
| Streamlit | Web app deployment |
| Pickle | Model serialization |

---

## 🧠 ML Pipeline

1. **Data Collection** — Gulf market used car dataset (Saudi Arabia)
2. **Data Cleaning** — Handled missing values, removed outliers, dropped irrelevant columns
3. **Feature Engineering** — Converted prices from SAR to QAR, applied One-Hot Encoding
4. **Model Training** — Random Forest Regressor
5. **Evaluation** — R² Score: **0.89**
6. **Deployment** — Streamlit Cloud

---

## 📊 Model Performance

| Metric | Value |
|--------|-------|
| R² Score | 0.89 |
| Algorithm | Random Forest Regressor |
| Training set | 80% |
| Testing set | 20% |

---

## 🚀 Run Locally

```bash
git clone https://github.com/vksox1404-web/car-price-predictor
cd car-price-predictor
pip install -r requirements.txt
streamlit run app.py
```

---

## 📁 Project Structure

```
car-price-predictor/
├── app.py                      # Streamlit web app
├── model.pkl                   # Trained ML model
├── columns.pkl                 # Feature columns
├── requirements.txt            # Dependencies
└── Car_Price_Prediction.ipynb  # Full ML notebook
```

---

## 👤 Author

**Ali Mohamed** — CS Graduate | AI & ML Enthusiast | Qatar

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](linkedin.com/in/ali-mohamed-5777b2403)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black)](https://github.com/vksox1404-web)
