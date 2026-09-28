import streamlit as st
from datetime import date

st.title("User Information")

name = st.text_input("Enter your name")

age = st.number_input("Enter your age", min_value=1, max_value=100)

dob = st.date_input(
    "Enter your date of birth",
    min_value=date(1900, 1, 1),
    max_value=date.today(),
    value=date(2000, 1, 1)  # default value
)

gender = st.selectbox(
    "Select gender",
    ["Male", "Female", "Other"]
)

email = st.text_input("Enter your email address")

course = st.selectbox("Select course", ["testing", "java", "python", "dotnet"])

btn = st.button("Submit")

if btn:
    st.write("Name:", name)
    st.write("Age:", age)
    st.write("Gender:", gender)
    st.write("Email:", email)
    st.write("Course:", course)
    st.write("DoB:", dob)
