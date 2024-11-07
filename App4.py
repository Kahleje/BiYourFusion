import streamlit as st
import pandas as pd
import datetime

# Set page background and custom styles
st.markdown(
    """
    <style>
    /* Background color gradient */
    .main {
        background: linear-gradient(to bottom right, #ffecd2, #fcb69f);
        font-family: 'Arial', sans-serif;
    }

    /* Title and headers styling */
    h1 {
        color: #E63946;
        font-size: 3em;
        text-align: center;
    }
    h2, h3 {
        color: #1D3557;
    }

    /* Container for data entry */
    .stTextInput, .stNumberInput, .stDateInput {
        border: 1px solid #457B9D;
        border-radius: 8px;
    }

    /* Tabs styling */
    .css-1ht1j8u, .css-1ht1j8u a {
        color: #1D3557;
        font-weight: bold;
    }

    /* Success and warning message styles */
    .stAlert {
        border-radius: 8px;
    }
    .stAlert-success {
        background-color: #A8DADC;
        color: #1D3557;
    }
    .stAlert-warning {
        background-color: #F1FAEE;
        color: #E63946;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App Title with styled header
st.title("BiYourFusion - Health Tracker App")

# Section 1: User Input
st.header("User Health Data Entry")

# User information inputs
user_name = st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value=0, max_value=120, value=25)
weight = st.number_input("Enter your weight (kg)", min_value=0.0, max_value=300.0, value=70.0)
height = st.number_input("Enter your height (cm)", min_value=0.0, max_value=250.0, value=170.0)

# Daily tracking data
st.header("Daily Tracking")
date = st.date_input("Select date", datetime.date.today())
steps = st.number_input("Enter steps walked", min_value=0, value=0)
calories = st.number_input("Enter calories consumed", min_value=0, value=0)
sleep = st.number_input("Enter hours slept", min_value=0.0, max_value=24.0, value=8.0)

# Store data in a DataFrame
data = {"Date": [date], "Steps": [steps], "Calories": [calories], "Sleep (hrs)": [sleep]}
df = pd.DataFrame(data)

# Display user data
st.subheader(f"Data for {user_name}")
st.write(f"Age: {age}, Weight: {weight} kg, Height: {height} cm")
st.dataframe(df)

# Section 2: Calculate BMI
st.header("Health Metrics")
if weight > 0 and height > 0:
    bmi = weight / ((height / 100) ** 2)
    st.write(f"Your BMI is: {bmi:.2f}")

# Section 3: Health Goal Tracking
st.header("Set Your Health Goals")
goal_steps = st.number_input("Daily Steps Goal", min_value=0, value=10000)
goal_calories = st.number_input("Daily Calories Goal", min_value=0, value=2000)
goal_sleep = st.number_input("Daily Sleep Goal (hrs)", min_value=0.0, max_value=24.0, value=8.0)

# Track Progress
st.subheader("Daily Progress")
if steps >= goal_steps:
    st.success(f"Great! You've reached your steps goal of {goal_steps} steps.")
else:
    st.warning(f"Keep going! You need {goal_steps - steps} more steps to reach your goal.")

if calories <= goal_calories:
    st.success("Good job! You've stayed within your calorie goal.")
else:
    st.warning(f"You've exceeded your calorie goal by {calories - goal_calories} calories.")

if sleep >= goal_sleep:
    st.success("Well done on hitting your sleep goal!")
else:
    st.warning(f"Try to get {goal_sleep - sleep} more hours of sleep.")

# Run the app with: `streamlit run app.py`