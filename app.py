import pandas as pd
import pickle
import streamlit as st

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

# Streamlit app
def main():
    st.title("BMI Tracker")

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
        else:
            st.error("Please enter valid inputs.")

if __name__ == '__main__':
    main()
