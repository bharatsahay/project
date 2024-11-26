import streamlit as st
import pickle
import numpy as np

# Load the pre-trained model (make sure you have the 'model.pkl' file in your working directory)
with open('model_RF.pkl', 'rb') as file:
    model = pickle.load(file)

# Function to convert user input into numeric format
def convert_user_input(gender, age, smoking, yellow_fingers, anxiety, peer_pressure, chronic_disease, fatigue, allergy, wheezing, alcohol_consuming, coughing, shortness_of_breath, swallowing_difficulty, chest_pain):
    gender = 1 if gender.lower() == 'male' else 2
    smoking = 1 if smoking.lower() == 'yes' else 0
    yellow_fingers = 1 if yellow_fingers.lower() == 'yes' else 0
    anxiety = 1 if anxiety.lower() == 'yes' else 0
    peer_pressure = 1 if peer_pressure.lower() == 'yes' else 0
    chronic_disease = 1 if chronic_disease.lower() == 'yes' else 0
    fatigue = 1 if fatigue.lower() == 'yes' else 0
    allergy = 1 if allergy.lower() == 'yes' else 0
    wheezing = 1 if wheezing.lower() == 'yes' else 0
    alcohol_consuming = 1 if alcohol_consuming.lower() == 'yes' else 0
    coughing = 1 if coughing.lower() == 'yes' else 0
    shortness_of_breath = 1 if shortness_of_breath.lower() == 'yes' else 0
    swallowing_difficulty = 1 if swallowing_difficulty.lower() == 'yes' else 0
    chest_pain = 1 if chest_pain.lower() == 'yes' else 0

    return [gender, age, smoking, yellow_fingers, anxiety, peer_pressure, chronic_disease, fatigue, allergy, wheezing, alcohol_consuming, coughing, shortness_of_breath, swallowing_difficulty, chest_pain]

# Custom CSS styling for the app
st.set_page_config(page_title="Lung Cancer Prediction App", page_icon="🎗️", layout="centered")
st.markdown(
    """
    <style>
    body {
        background-color: #1e1e1e;
    }
    .main:before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: url('D:\7th Sem\backround.jpeg');
        background-size: cover;
        background-repeat: no-repeat;
        opacity: 0.3;
        z-index: -1;
    }
    .main > * {
        position: relative;
        z-index: 2;
    }
    .title {
        font-size: 40px;
        font-weight: bold;
        color: #f39c12;
        text-align: center;
    }
    .subheader {
        font-size: 20px;
        color: #7f8c8d;
        text-align: center;
        margin-bottom: 20px;
    }
    .input_label {
        font-size: 16px;
        color: #ecf0f1;
    }
    .button {
        background-color: #e67e22;
        color: white;
        font-size: 18px;
        padding: 10px;
        border-radius: 10px;
    }
    .result {
        font-size: 20px;
        font-weight: bold;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
    }
    .result.red {
        background-color: #e74c3c;
        color: white;
    }
    .result.green {
        background-color: #27ae60;
        color: white;
    }
    .stTextInput, .stSelectbox, .stButton {
        background-color: #3c3c3c !important;
        border: 1px solid #555 !important;
        color: #ecf0f1 !important;
        padding: 10px !important;
        border-radius: 5px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

#                           


# Main container for the app
st.markdown("<div class='main'>", unsafe_allow_html=True)
st.markdown("<div class='title'>Lung Cancer Prediction App</div>", unsafe_allow_html=True)
st.markdown("<div class='subheader'>Enter your details to predict the risk of lung cancer</div>", unsafe_allow_html=True)

# Creating an interactive user input form
with st.form(key='input_form'):
    st.markdown("**Please fill in the following details:**")
    
    # Create a layout with two columns
    col1, col2 = st.columns(2)
    
    # Collect inputs
    with col1:
        gender = st.selectbox("Gender", ['Male', 'Female'])
        age = st.slider("Age", min_value=18, max_value=100, value=30)
        smoking = st.selectbox("Do you smoke?", ['Yes', 'No'])
        yellow_fingers = st.selectbox("Do you have yellow fingers?", ['Yes', 'No'])
        anxiety = st.selectbox("Do you have anxiety?", ['Yes', 'No'])
        peer_pressure = st.selectbox("Do you experience peer pressure?", ['Yes', 'No'])
        chronic_disease = st.selectbox("Do you have chronic diseases?", ['Yes', 'No'])

    with col2:
        fatigue = st.selectbox("Do you have fatigue?", ['Yes', 'No'])
        allergy = st.selectbox("Do you have allergies?", ['Yes', 'No'])
        wheezing = st.selectbox("Do you experience wheezing?", ['Yes', 'No'])
        alcohol_consuming = st.selectbox("Do you consume alcohol?", ['Yes', 'No'])
        coughing = st.selectbox("Do you have a cough?", ['Yes', 'No'])
        shortness_of_breath = st.selectbox("Do you experience shortness of breath?", ['Yes', 'No'])
        swallowing_difficulty = st.selectbox("Do you have difficulty swallowing?", ['Yes', 'No'])
        chest_pain = st.selectbox("Do you have chest pain?", ['Yes', 'No'])

    # Submit button
    submit_button = st.form_submit_button(label='Predict Lung Cancer')

# Convert user input to a format the model can understand
if submit_button:
    user_input = convert_user_input(gender, age, smoking, yellow_fingers, anxiety, peer_pressure, chronic_disease, fatigue, allergy, wheezing, alcohol_consuming, coughing, shortness_of_breath, swallowing_difficulty, chest_pain)
    
    # Reshape the input for the model
    input_array = np.array(user_input).reshape(1, -1)
    
    # Make the prediction using the model
    prediction = model.predict(input_array)
    
    # Display prediction result with style
    if prediction == 1:
        st.markdown(f"<div class='result red'>⚠️ The model predicts that you may have lung cancer!</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='result green'>✅ The model predicts that you do not have lung cancer.</div>", unsafe_allow_html=True)

    st.balloons()  # Add a celebration effect when the result is shown

st.markdown("</div>", unsafe_allow_html=True)
