# Display the logged data
st.subheader("Logged Data")
st.dataframe(st.session_state.health_data)
import streamlit as st
import pandas as pd
st.title("BiYourFusion")
st.header("Log Your Daily Health Metrics")
# Initialize DataFrame to store data
if "health_data" not in st.session_state:
    st.session_state.health_data = pd.DataFrame(columns=["Date", "Weight (kg)", "Steps"])
# Inputs for health metrics
date = st.date_input("Select Date")
weight = st.number_input("Enter your weight (in kg):", min_value=0.0, step=0.1)
steps = st.number_input("How many steps did you take today?", min_value=0)
# Submit button to log data
if st.button("Submit"):
    new_entry = pd.DataFrame([[date, weight, steps]], columns=["Date", "Weight (kg)", "Steps"])
    st.session_state.health_data = pd.concat([st.session_state.health_data, new_entry], ignore_index=True)
    st.write("Entry logged successfully!")
# Display the logged data
st.subheader("Logged Data")
st.dataframe(st.session_state.health_data)
# Display a line chart of steps over time
if not st.session_state.health_data.empty:
    st.subheader("Steps Trend")
    st.line_chart(st.session_state.health_data.set_index("Date")["Steps"])
import streamlit as st
import pandas as pd
st.title("BiYourFusion")
# Create two columns
col1, col2 = st.columns(2)
with col1:
    st.header("Log Your Data")
    date = st.date_input("Select Date")
    weight = st.number_input("Enter your weight (in kg):", min_value=0.0, step=0.1)
    steps = st.number_input("How many steps did you take today?", min_value=0)
    if st.button("Submit"):
        new_entry = pd.DataFrame([[date, weight, steps]], columns=["Date", "Weight (kg)", "Steps"])
        st.session_state.health_data = pd.concat([st.session_state.health_data, new_entry], ignore_index=True)
        st.write("Entry logged successfully!")
with col2:
    st.header("Logged Data")
    if "health_data" not in st.session_state:
        st.session_state.health_data = pd.DataFrame(columns=["Date", "Weight (kg)", "Steps"])
    st.dataframe(st.session_state.health_data)
    if not st.session_state.health_data.empty:
        st.subheader("Steps Trend")
        st.line_chart(st.session_state.health_data.set_index("Date")["Steps"])