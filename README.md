# 🏋️‍♂️ BMI Tracker 🏋️‍♀️

Welcome to the BMI Tracker app! 🌟 This app predicts your BMI category based on your gender, height, and weight. The model is built using Random Forest Classifier and provides an easy way to determine if you're underweight, normal, overweight, or in another category. 💪

## 🌟 Features 🌟

- **BMI Prediction**: Predict your BMI category (e.g., Normal, Overweight, Obesity) based on the data you input. 📊
- **Machine Learning Model**: A Random Forest Classifier model makes accurate predictions. 🤖
- **Streamlit Web App**: The app is built using Streamlit for an interactive UI. 💻

## 📋 Requirements 📋

To run this project locally, make sure you have Python installed and the following dependencies:
- pandas
- scikit-learn
- pickle
- streamlit

Install them using pip:

```bash
pip install pandas scikit-learn streamlit
```

## 🗂️ Files 🗂️

- `bmi.csv`: The dataset used to train the Random Forest model. 📊
- `trained_model.sav`: The saved model after training. 💾
- `app.py`: The Streamlit app file to run the BMI Tracker. 🖥️
- `README.md`: This file, explaining the project. 📄

## 🚀 How to Run 🚀

1. Install the necessary dependencies (as mentioned above).
2. Place the dataset file (`bmi.csv`) and the trained model file (`trained_model.sav`) in the same directory as the `app.py` file.
3. Run the app with the following command:

```bash
streamlit run app.py
```

This will launch a local server and open the app in your default browser. 🌐

## 🤖 Model Details 🤖

The model used in this app is a Random Forest Classifier that predicts the BMI category based on the input data:

### Features
- Gender
- Height
- Weight

### Target: BMI category (0 to 5)

BMI Categories:
- 0: Extremely Weak 🦸‍♂️
- 1: Weak 💪
- 2: Normal ⚖️
- 3: Overweight 🍔
- 4: Obesity 🍩
- 5: Extreme Obesity 🍕

The model was trained using a dataset of individuals' gender, height, weight, and BMI categories. 📚

## 💡 Usage 💡

### Streamlit Interface:
- **Gender**: Select your gender (Male or Female). 👦👧
- **Height**: Enter your height in centimeters (range: 50 to 250 cm). 📏
- **Weight**: Enter your weight in kilograms (range: 10 to 200 kg). ⚖️
- **Calculate BMI**: After filling in the fields, click the Calculate BMI button to predict your BMI category. 🧮

### Example Prediction:
- **Gender**: Male 👨
- **Height**: 175 cm 📏
- **Weight**: 70 kg ⚖️

**Predicted BMI Category**: Normal ⚖️

## ⚠️ Troubleshooting ⚠️

- Ensure the `bmi.csv` and `trained_model.sav` files are correctly placed in the same directory as `app.py`. 📂
- If you're encountering issues with inputs, make sure to provide valid numbers for height and weight. 🧐

## 📜 License 📜

This project is licensed under the MIT License. See the LICENSE file for more details. 📃
