import streamlit as st

st.title("🎸 Band Name Generator")

city = st.text_input("Enter your city name:")
pet = st.text_input("Enter your pet name:")

if city and pet:
    st.success(f"Your Band Name is: {city} {pet}")
