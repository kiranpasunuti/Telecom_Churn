import streamlit as st
import pandas as pd
import pickle

# Load the model using pickle
with open("RandomForest_Churn_Model.pkl", "rb") as file:
    model_RF = pickle.load(file)

# Define the input fields
input_columns = ['voice.plan', 'voice.messages', 'intl.plan', 'intl.mins', 'intl.calls', 'intl.charge',
                 'day.mins', 'day.charge', 'eve.mins', 'eve.charge', 'night.mins', 'night.charge', 'customer.calls']

# First page layout
st.title("Telecom Churn Prediction")

# Create a dictionary to store user input
user_input = {}

# Collect user inputs on the first page
for col in input_columns:
    user_input[col] = st.number_input(f"Enter {col}", value=0.0)

# Validate input data
input_df = pd.DataFrame([user_input])

# Ensure input data has the correct column names and order
if not input_df.columns.equals(pd.Index(input_columns)):
    st.error(f"Input data must have columns in the following order: {', '.join(input_columns)}")
else:
    # Predict button
    if st.button("Predict"):
        # Make prediction
        prediction = model_RF.predict(input_df)[0]

        # Display result on the same page
        st.title("Churn Prediction Result")

        # Display result with animation or other visualizations
        if prediction == 1:
            st.success("Churn: This customer is likely to churn.")
            # Add animations or visualizations for churn
        else:
            st.success("Not Churn: This customer is not likely to churn.")
            # Add animations or visualizations for not churn
