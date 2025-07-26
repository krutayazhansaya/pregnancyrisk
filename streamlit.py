import streamlit as st
import requests

st.title("Pregnancy Risk Prediction")
st.write("Adjust the values below to predict pregnancy complication risk.")

# Sliders for numerical inputs
age = st.slider("Age", 10, 100, 30)
systolic_bp = st.slider("Systolic Blood Pressure", 70, 200, 120)
diastolic = st.slider("Diastolic Blood Pressure", 40, 140, 80)
bs = st.slider("Blood Sugar (BS)", 3, 15, 6)
body_temp = st.slider("Body Temperature (°F)", 97, 103, 98)
bmi = st.slider("BMI", 15, 35, 22)
heart_rate = st.slider("Heart Rate", 60, 100, 75)

# Checkboxes for binary fields
previous_complications = st.checkbox("Previous Complications")
preexisting_diabetes = st.checkbox("Preexisting Diabetes")
gestational_diabetes = st.checkbox("Gestational Diabetes")
mental_health = st.checkbox("Mental Health Issues")

# Convert checkboxes to 0/1
previous_complications = int(previous_complications)
preexisting_diabetes = int(preexisting_diabetes)
gestational_diabetes = int(gestational_diabetes)
mental_health = int(mental_health)

# Button to trigger prediction
if st.button("Predict Risk"):
    payload = {
        "Age": age,
        "Systolic BP": systolic_bp,
        "Diastolic": diastolic,
        "BS": bs,
        "Body Temp": body_temp,
        "BMI": bmi,
        "Previous Complications": previous_complications,
        "Preexisting Diabetes": preexisting_diabetes,
        "Gestational Diabetes": gestational_diabetes,
        "Mental Health": mental_health,
        "Heart Rate": heart_rate
    }

    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=payload)
        result = response.json()
        if response.status_code == 200:
            st.success(f"Prediction: {'High Risk' if result['prediction'] == 1 else 'Low Risk'}")
            st.write(f"Probability of risk: {result['probability']:.2f}")
        else:
            st.error(f"Prediction failed: {result['detail']}")
    except Exception as e:
        st.error(f"Error connecting to the prediction API: {str(e)}")
