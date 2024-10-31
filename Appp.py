import streamlit as st

def main():
    # Title and description
    st.title("Welcome to Your Health & Fitness Hub")
    st.write("""
    This is your all-in-one platform for fitness, mental health, nutrition, and wellness.
    """)

    # Sections for different features
    st.header("Features")
    st.write("Explore the key features of our app:")
    
    st.subheader("🧘 Mental Health")
    st.write("Guided meditations, journaling, and mindfulness activities.")

    st.subheader("🍎 Nutrition")
    st.write("Personalized meal plans and nutrition tips to fuel your body.")

    st.subheader("💪 Fitness")
    st.write("Workout routines and exercises tailored to your goals.")

    st.subheader("🛌 Wellness")
    st.write("Sleep tracking, water intake reminders, and more.")

if __name__ == "__main__":
    main()
