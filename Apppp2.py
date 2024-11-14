import streamlit as st
import pandas as pd
import datetime

# Custom styling for the info box with a blue background
st.markdown(
    """
    <style>
    /* Gradient background */
    .main {
        background: linear-gradient(135deg, #00C9FF, #92FE9D);
        font-family: 'Arial', sans-serif;
    }

    /* Title and headers styling */
    h1, h2, h3 {
        color: #FFFFFF;
    }

    /* Input fields styling */
    .stTextInput, .stNumberInput, .stDateInput {
        background-color: #F0F0F0;
        border: 1px solid #FFFFFF;
        border-radius: 8px;
    }

    /* Message styling */
    .stAlert-success {
        background-color: #00A8CC;
        color: #FFFFFF;
    }
    .stAlert-warning {
        background-color: #FFE15D;
        color: #FFFFFF;
    }

    /* Custom styling for instructions */
    .run-instruction {
        font-size: 18px;
        color: #FFFFFF;
        background-color: #007BFF; /* Blue background */
        border-left: 4px solid #FFFFFF;
        padding: 10px;
        font-weight: bold;
        font-family: 'Arial', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Set up the app title and content
st.title("BiYourFusion - Health Tracker App")

# Display the instruction with the custom class
st.markdown('<div class="run-instruction">Run the app with: <code>streamlit run app.py</code></div>', unsafe_allow_html=True)

# Set up the app title and content
st.title("BiYourFusion - Health Tracker App")

# Display the instruction with the custom class
st.markdown('<div class="run-instruction">Run the app with: <code>streamlit run app.py</code></div>', unsafe_allow_html=True)


# Set up the app title and content
st.title("BiYourFusion - Health Tracker App")

# ... [rest of your app code here] ...
import streamlit as st
import pandas as pd
import datetime

# Image background styling
st.markdown(
    """
    <style>
    /* Background image */
    .main {
        background-image: url("fitness_background.jpg");
        background-size: cover;
        background-position: center;
        font-family: 'Arial', sans-serif;
    }

    /* Title and headers styling */
    h1, h2, h3 {
        color: #FFFFFF;
        text-shadow: 2px 2px 4px #000000;
    }

    /* Input fields styling */
    .stTextInput, .stNumberInput, .stDateInput {
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 8px;
    }

    /* Alert messages styling */
    .stAlert-success {
        background-color: rgba(34, 139, 34, 0.9);
        color: #FFFFFF;
    }
    .stAlert-warning {
        background-color: rgba(255, 69, 0, 0.9);
        color: #FFFFFF;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Set up the app title and content
st.title("BiYourFusion - Health Tracker App")

# ... [rest of your app code here] ...
import streamlit as st
import pandas as pd
import datetime

# Set up the app title
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
import streamlit as st
import pandas as pd
import datetime

# App Title
st.title("BiYourFusion - In-depth Health Tracker")

# Sidebar for category selection
with st.sidebar:
    st.header("Navigation")
    option = st.radio("Go to:", ["Daily Tracking", "Progress Charts", "Goals", "Settings"])

# ---- Daily Tracking ----
if option == "Daily Tracking":
    st.header("Daily Tracking")

    # Sidebar inputs for Daily Tracking
    with st.sidebar:
        st.subheader("Daily Tracking Inputs")
        date = st.date_input("Select date", datetime.date.today())
        steps = st.number_input("Steps walked", min_value=0, value=0)
        calories = st.number_input("Calories consumed", min_value=0, value=0)
        sleep = st.number_input("Hours slept", min_value=0.0, max_value=24.0, value=8.0)

    # Display entered data
    st.subheader("Today's Data")
    data = {"Date": [date], "Steps": [steps], "Calories": [calories], "Sleep (hrs)": [sleep]}
    daily_df = pd.DataFrame(data)
    st.write(daily_df)

# ---- Progress Charts ----
elif option == "Progress Charts":
    st.header("Progress Charts")

    # Placeholder data for historical tracking
    dates = pd.date_range(start="2023-01-01", periods=30)
    steps_data = [5000 + i*200 for i in range(30)]  # Simulated step data
    calories_data = [2000 - i*10 for i in range(30)]  # Simulated calorie data
    sleep_data = [7 + (i % 3) for i in range(30)]  # Simulated sleep data

    # Create a DataFrame with sample data
    progress_df = pd.DataFrame({
        "Date": dates,
        "Steps": steps_data,
        "Calories": calories_data,
        "Sleep (hrs)": sleep_data
    })

    # Sidebar inputs for chart filters (optional)
    with st.sidebar:
        st.subheader("Chart Settings")
        st.write("Adjust chart settings here if needed.")

    # Plotting the data
    st.line_chart(progress_df.set_index("Date"))

# ---- Goals ----
elif option == "Goals":
    st.header("Set Your Health Goals")

    # Sidebar inputs for setting goals
    with st.sidebar:
        st.subheader("Set Goals")
        goal_steps = st.number_input("Daily Steps Goal", min_value=0, value=10000)
        goal_calories = st.number_input("Daily Calories Goal", min_value=0, value=2000)
        goal_sleep = st.number_input("Daily Sleep Goal (hrs)", min_value=0.0, max_value=24.0, value=8.0)

    # Display current goals
    st.subheader("Current Goals")
    st.write(f"Steps Goal: {goal_steps} steps")
    st.write(f"Calories Goal: {goal_calories} calories")
    st.write(f"Sleep Goal: {goal_sleep} hours")

# ---- Settings ----
elif option == "Settings":
    st.header("Settings")

    # Sidebar inputs for profile information
    with st.sidebar:
        st.subheader("Profile Settings")
        user_name = st.text_input("Enter your name")
        age = st.number_input("Enter your age", min_value=0, max_value=120, value=25)
        weight = st.number_input("Enter your weight (kg)", min_value=0.0, max_value=300.0, value=70.0)
        height = st.number_input("Enter your height (cm)", min_value=0.0, max_value=250.0, value=170.0)

    # Display user profile
    st.subheader("Profile Information")
    st.write(f"Name: {user_name}")
    st.write(f"Age: {age}")
    st.write(f"Weight: {weight} kg")
    st.write(f"Height: {height} cm")

# Instructions to run the app
st.info("Run the app with: `streamlit run app.py`")
