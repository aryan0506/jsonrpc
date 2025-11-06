import streamlit as st
import requests

API_URL = "http://localhost:8000/predict"
st.title("House Price Predictor")
st.markdown("Enter the details of the house to predict its price.")

#input fields for user to enter data
med_inc = st.number_input("Median Income", min_value=0.0)
house_age = st.number_input("House Age", min_value=0.0)
ave_rooms = st.number_input("Average Rooms", min_value=0.0)
ave_bedrms = st.number_input("Average Bedrooms", min_value=0.0)
population = st.number_input("Population", min_value=0.0)
ave_occup = st.number_input("Average Occupancy", min_value=0.0) 
latitude = st.number_input("Latitude", min_value=-90.0, max_value=90.0)
longitude = st.number_input("Longitude", min_value=-180.0, max_value=180.0)
 
if st.button("Predict Price"):
    input_data = {
        "MedInc": med_inc,
        "HouseAge": house_age,
        "AveRooms": ave_rooms,
        "AveBedrms": ave_bedrms,
        "Population": population,
        "AveOccup": ave_occup,
        "Latitude": latitude,
        "Longitude": longitude
    }
    response = requests.post(API_URL, json=input_data)
    if response.status_code == 200:
        prediction = response.json().get("predicted_price")
        st.success(f"The predicted house price is: ${prediction:,.2f}")
    else:
        st.error("Error in prediction. Please check the input values.")
        st.write(response.text)

