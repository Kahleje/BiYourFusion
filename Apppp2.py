

# Set up the title and main sections
st.title("Integrated Health App")
st.sidebar.title("Explore")

# Sidebar options
sections = ["Home", "Mental Health", "Fitness", "Nutrition", "Wellness"]
choice = st.sidebar.selectbox("Navigate", sections)

# Route based on selection
if choice == "Home":
    st.write("Welcome to the Integrated Health App!")
    st.write("An all-in-one platform for mental health, nutrition, fitness, and wellness.")

elif choice == "Mental Health":
    mental_health.display()

elif choice == "Fitness":
    fitness.display()

elif choice == "Nutrition":
    nutrition.display()

elif choice == "Wellness":
    wellness.display()
