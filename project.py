
import streamlit as st

st.title("Unit Converter App")
st.markdown("### Converts units of length, weight, and time instantly")
st.write("Welcome! Select a category, enter the value, and get the converted result in real time")

category = st.selectbox("Choose a category", ["length", "weight", "time"])

def convert_units(category, value, unit):
    if category == "length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371
    elif category == "weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462
    elif category == "time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24

if category == "length":
    unit = st.selectbox("Select unit", ["Kilometers to Miles", "Miles to Kilometers"])
elif category == "weight":
    unit = st.selectbox("Select unit", ["Kilograms to Pounds", "Pounds to Kilograms"])
elif category == "time":
    unit = st.selectbox("Select unit", ["Seconds to Minutes", "Minutes to Seconds", "Minutes to Hours", "Hours to Minutes", "Hours to Days", "Days to Hours"])

value = st.number_input("Enter the value to convert")

if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"{value} {unit} is equal to {result:.2f}")