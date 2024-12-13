import pandas as pd
import pickle
import streamlit as st
import datetime

# Load the saved model
loaded_model = pickle.load(open("C:/Users/harik/OneDrive/Desktop/Desktop/Desktop Projects/BMI APP/trained_model.sav", 'rb'))

# Mapping for BMI categories
bmi_category_mapping = {
    0: "Extremely Weak",
    1: "Weak",
    2: "Normal",
    3: "Overweight",
    4: "Obesity",
    5: "Extreme Obesity"
}

# Suggested diet plans
detailed_diet_plans = {
    "Extremely Weak": {
        "Vegetarian": "Paneer tikka, dal makhani, avocado toast, nuts, and seeds.",
        "Non-Vegetarian": "Chicken curry, salmon, eggs with whole-grain toast, and yogurt smoothies.",
        "Vegan": "Peanut butter on gluten-free bread, quinoa bowls with roasted vegetables, and almond milk smoothies.",
        "Gluten-Free": "Brown rice with beans, sweet potatoes, gluten-free pasta with pesto."
    },
    "Weak": {
        "Vegetarian": "Vegetable pulao, cheese sandwiches, Greek salad with olives, and milkshakes.",
        "Non-Vegetarian": "Grilled chicken, scrambled eggs with veggies, and turkey sandwiches.",
        "Vegan": "Chickpea curry with coconut milk, tofu stir-fry, and almond butter smoothies.",
        "Gluten-Free": "Lentil soup, baked potatoes with olive oil, and roasted zucchini."
    },
    "Normal": {
        "Vegetarian": "Spinach paratha, mixed vegetable curry, and fruit salads.",
        "Non-Vegetarian": "Grilled fish, chicken salads, and omelets with whole-grain toast.",
        "Vegan": "Buddha bowls with quinoa, sautéed kale, and tempeh wraps.",
        "Gluten-Free": "Quinoa salad, baked salmon with asparagus, and roasted chickpeas."
    },
    "Overweight": {
        "Vegetarian": "Cucumber and carrot salads, poha, and steamed vegetables.",
        "Non-Vegetarian": "Grilled chicken breast, boiled eggs, and fish soups.",
        "Vegan": "Zucchini noodles with tomato sauce, smoothies with almond milk, and tofu salads.",
        "Gluten-Free": "Cauliflower rice, lentil patties, and gluten-free vegetable soups."
    },
    "Obesity": {
        "Vegetarian": "Lentil soups, steamed broccoli, and salads with olive oil dressing.",
        "Non-Vegetarian": "Baked salmon, boiled chicken with green beans, and tuna salads.",
        "Vegan": "Spinach and chickpea curry, roasted Brussels sprouts, and avocado salads.",
        "Gluten-Free": "Sweet potato mash, grilled eggplant, and gluten-free zucchini noodles."
    },
    "Extreme Obesity": {
        "Vegetarian": "Small portions of dals, low-oil vegetable soups, and sprout salads.",
        "Non-Vegetarian": "Grilled chicken with lemon, steamed fish, and boiled eggs.",
        "Vegan": "Steamed edamame, kale chips, and roasted vegetables.",
        "Gluten-Free": "Gluten-free crackers, boiled quinoa, and roasted pumpkin."
    }
}

# Suggested exercises
exercise_plans = {
    "Extremely Weak": "Light yoga and stretching exercises.",
    "Weak": "Walking, light jogging, and yoga.",
    "Normal": "Moderate workouts like running, cycling, or swimming.",
    "Overweight": "Low-impact exercises like brisk walking or water aerobics.",
    "Obesity": "Low-intensity exercises under supervision.",
    "Extreme Obesity": "Medical consultation for supervised exercise plans."
}

# Function to predict BMI category
def predict_bmi(gender, height, weight):
    try:
        # Encode gender to match the model input
        gender_encoded = 1 if gender.lower() == "male" else 0

        # Prepare the input data as a DataFrame
        input_data = pd.DataFrame([[gender_encoded, height, weight]], columns=['Gender', 'Height', 'Weight'])

        # Make prediction
        predicted_class = loaded_model.predict(input_data)[0]

        # Get the BMI category
        return bmi_category_mapping[predicted_class]
    except Exception as e:
        return f"Error: {str(e)}"

# Function for health tips
def daily_health_tip():
    tips = [
        "Drink at least 8 glasses of water daily.",
        "Incorporate at least 30 minutes of physical activity daily.",
        "Focus on whole foods like fruits, vegetables, and lean proteins.",
        "Avoid processed foods and sugary drinks.",
        "Get at least 7-8 hours of sleep every night."
    ]
    return tips[datetime.datetime.now().day % len(tips)]

# Streamlit app
def main():
    st.title("BMI Tracker PAL")

    # Collect user input
    gender = st.selectbox("Select Gender", ["Male", "Female"])
    height = st.number_input("Enter Height (in cm)", min_value=50.0, max_value=250.0, step=0.1)
    weight = st.number_input("Enter Weight (in kg)", min_value=10.0, max_value=200.0, step=0.1)

    # Prediction result
    if st.button('Calculate BMI'):
        if gender and height > 0 and weight > 0:
            result = predict_bmi(gender, height, weight)
            if "Error" in result:
                st.error(result)
            else:
                st.success(f"Predicted BMI Category: {result}")

                # Display detailed diet plan
                st.markdown("### Suggested Diet Plan")
                dietary_preference = st.selectbox("Dietary Preference", ["Vegetarian", "Non-Vegetarian", "Vegan", "Gluten-Free"])
                if dietary_preference in detailed_diet_plans[result]:
                    st.info(detailed_diet_plans[result][dietary_preference])
                else:
                    st.info("No specific plan available for this preference.")

                # Display exercise plan
                st.markdown("### Suggested Exercises")
                st.info(exercise_plans[result])
        else:
            st.error("Please enter valid inputs.")

    # Sidebar for additional features
    st.sidebar.title("Advanced Features")

    # Health Tips
    with st.sidebar.expander("Daily Health Tip"):
        st.write(daily_health_tip())

    # Exercise Tracking
    with st.sidebar.expander("Exercise Tracker"):
        workout_duration = st.number_input("Enter Workout Duration (minutes)", min_value=0, step=5)
        if workout_duration:
            st.write(f"You worked out for {workout_duration} minutes today!")

    # Calorie Tracker
    with st.sidebar.expander("Calorie Tracker"):
        calorie_intake = st.number_input("Enter Today's Calorie Intake (kcal)", min_value=0, step=50)
        st.write(f"Calories Consumed Today: {calorie_intake} kcal")

    # Water Intake Tracker
    with st.sidebar.expander("Water Intake Tracker"):
        water_intake = st.number_input("Enter Water Intake (in liters)", min_value=0.0, max_value=10.0, step=0.1)
        st.write(f"Water Consumed Today: {water_intake} liters")

    # Progress Tracking
    with st.sidebar.expander("Progress Tracking"):
        weight_progress = st.number_input("Log Your Current Weight (kg)", min_value=10.0, max_value=200.0, step=0.1)
        waist_measurement = st.number_input("Log Your Waist Measurement (cm)", min_value=10.0, max_value=200.0, step=0.1)
        st.write(f"Current Weight: {weight_progress} kg")
        st.write(f"Waist Measurement: {waist_measurement} cm")

    # Gamification
    with st.sidebar.expander("Gamification"):
        streak_days = st.slider("Current Streak (Days)", min_value=0, max_value=100)
        st.write(f"Your Streak: {streak_days} Days")
        if streak_days > 0:
            st.success("Great job! Keep it up!")
        else:
            st.warning("Start your journey today!")

if __name__ == '__main__':
    main()
