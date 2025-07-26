# pregnancyrisk
Likelihood of pregnancy risk
# 🤰 Pregnancy Risk Prediction App

A Machine Learning web application built with **FastAPI** and **Streamlit** to **predict the probability of pregnancy complications** based on a woman's health data.

---

## 📌 About the Project

Every 2 minutes, a woman dies from complications related to pregnancy and childbirth — most of them preventable.  
This project aims to **provide an early warning system** using machine learning to evaluate the **risk level during pregnancy**, helping patients and healthcare providers make informed decisions.

---

## 🚀 Features

- Predicts **risk of pregnancy complications** using trained ML models
- Built-in **FastAPI** backend and **Streamlit** frontend
- Real-time predictions and probability outputs
- Supports multiple health input parameters (Age, BP, BMI, etc.)
- Clean and user-friendly UI

---

## 🧠 Models Used

| Model                   | Accuracy | Precision | Recall   | F1 Score |
| ----------------------- | -------- | --------- | -------- | -------- |
| **Logistic Regression** | 0.97     | 0.94      | 0.97     | 0.95     |
| **Decision Tree**       | 0.97     | 0.98      | 0.94     | 0.96     |
| **CatBoost**            | **0.99** | **0.99**  | **0.98** | **0.98** |

✅ The **CatBoost** model was chosen for deployment due to its **highest performance**.

---

## 📂 Project Structure

