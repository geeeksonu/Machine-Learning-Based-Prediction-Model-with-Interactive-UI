import streamlit as st
from predict import display_salary_prediction
from explore import show_exp_pg

page = st.sidebar.selectbox("Explore or Predict", ("Predict", "Explore"))

if page == "Predict":
    display_salary_prediction()
else:
    show_exp_pg()
