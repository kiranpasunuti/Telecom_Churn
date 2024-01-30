import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from joblib import load

import sklearn
print(sklearn.__version__)

loaded_model = load("Tele_Com.joblib")

# Initialize session state
if 'show_result' not in st.session_state:
    st.session_state.show_result = False

# Define the input fields along with their corresponding input types and conditions
#input_columns = {
 #   'voice.plan': {'type': 'radio', 'options': [0, 1]},
  #  'voice.messages': {'type': 'number_input'},
   # 'intl.plan': {'type': 'radio', 'options': [0, 1]},
    #'intl.mins': {'type': 'number_input'},
#    'intl.calls': {'type': 'number_input'},
 #   'intl.charge': {'type': 'number_input'},
  #  'day.mins': {'type': 'number_input'},
   # 'day.charge': {'type': 'number_input'},
#    'eve.mins': {'type': 'number_input'},
 #   'eve.charge': {'type': 'number_input'},
#    'night.mins': {'type': 'number_input'},
#    'night.charge': {'type': 'number_input'},
#    'customer.calls': {'type': 'number_input'},
#}

input_columns = {
    'voice.plan': {'type': 'radio', 'text': 'Voice Plan', 'options': [0, 1]},
    'voice.messages': {'type': 'number_input', 'text': 'Voice Messages'},
    'intl.plan': {'type': 'radio', 'text': 'International Plan', 'options': [0, 1]},
    'intl.mins': {'type': 'number_input', 'text': 'International Minutes'},
    'intl.calls': {'type': 'number_input', 'text': 'International Calls'},
    'intl.charge': {'type': 'number_input', 'text': 'International Charge'},
    'day.mins': {'type': 'number_input', 'text': 'Day Minutes'},
    'day.charge': {'type': 'number_input', 'text': 'Day Charge'},
    'eve.mins': {'type': 'number_input', 'text': 'Evening Minutes'},
    'eve.charge': {'type': 'number_input', 'text': 'Evening Charge'},
    'night.mins': {'type': 'number_input', 'text': 'Night Minutes'},
    'night.charge': {'type': 'number_input', 'text': 'Night Charge'},
    'customer.calls': {'type': 'number_input', 'text': 'Customer Calls'},
}

# Create a dictionary to store user input
user_input = {}

# First page layout
st.title("Telecom Churn Prediction")

# Collect user inputs on the first page
for col, input_info in input_columns.items():
    if input_info['type'] == 'number_input':
        user_input[col] = st.number_input(f"{input_info['text']}", value=0, step=1)
    elif input_info['type'] == 'radio':
        # Map 'NO' to 0 and 'YES' to 1
        user_input[col] = 1 if st.radio(f"{input_info['text']}", options=input_info['options'], key=col) == 'YES' else 0


# Predict button
if st.button("Predict"):
    # Create a DataFrame from user input
    input_df = pd.DataFrame([user_input])

    # Make prediction
    prediction = loaded_model.predict(input_df)[0]

    # Set the session state variable to True to show the second page
    st.session_state.show_result = True

# Check if the button to show the second page is clicked
if st.session_state.show_result:
    # Page break
    st.markdown("---")

    # Second page layout
    st.title("Result")

    # Display result with animation or other visualizations
    if prediction == 1:
        st.markdown("this customer is likely to <span style='color:red; font-size:32px;'>CHURN</span>", unsafe_allow_html=True)
        # Add animations or visualizations for churn
        st.image('https://i.gifer.com/3n7y.gif', caption=" ", width=300)  # Set width to your preferred value
    else:
        st.markdown("this customer is likely to <span style='color:red; font-size:32px;'>NOT CHURN</span>", unsafe_allow_html=True)
        # Add animations or visualizations for not churn
        st.image("https://i.gifer.com/2DV.gif", caption=" ", width=300)  # Set width to your preferred value



