import streamlit as st
import pickle
import numpy as np



def fetch_model():
    with open('mlModel.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = fetch_model()

prediction_model = data["model"]
country_label_encoder = data["LableCountry"]
education_label_encoder = data["LableEducation"]


def display_salary_prediction():
    st.title("Predicting Software Developer Salary")

    st.write("""Provide Information for Salary Prediction""")

    countries = (
        "United States",
        "India",
        "United Kingdom",
        "Germany",
        "Canada",
        "Brazil",
        "France",
        "Spain",
        "Australia",
        "Netherlands",
        "Poland",
        "Italy",
        "Russian Federation",
        "Sweden",
    )

    education_levels = (
        "Less than a Bachelors",
        "Bachelor’s degree",
        "Master’s degree",
        "Post grad",
    )

    selected_country = st.selectbox("Country", countries)
    selected_education = st.selectbox("Education Level", education_levels)

    years_experience = st.slider("Years of Experience", 0, 50, 3)

    calculate_button = st.button("Calculate Salary")
    if calculate_button:
        input_data = np.array([[selected_country, selected_education, years_experience]])
        input_data[:, 0] = country_label_encoder.transform(input_data[:, 0])
        input_data[:, 1] = education_label_encoder.transform(input_data[:, 1])
        input_data = input_data.astype(float)

        predicted_salary = prediction_model.predict(input_data)
        st.subheader(f"Estimated Salary: ${predicted_salary[0]:.2f}")
