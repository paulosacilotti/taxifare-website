import streamlit as st
import datetime
import requests
import pandas as pd
import json
import pytz
from datetime import datetime

'''
UberPred - Prédire le prix d'une course 🚕
Bienvenue, entre ton adresse de départ et ton adresse d'arrivée, tu verras combien ça te coûte 💸
'''



default_latitude = 40.730610
default_longitude = -73.935242

pickup_longitude = st.number_input("Pick up longitude:", value=default_longitude)
pickup_latitude = st.number_input("Pick up latitude:", value=default_latitude)
dropoff_longitude = st.number_input("Drop off longitude:", value=default_longitude)
dropoff_latitude = st.number_input("Drop off latitude:", value=default_latitude)

passenger_count = st.number_input("number of passengers", value=1)



url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':


key = "2013-07-06 17:18:00.000000119"
    # localize the user provided datetime with the NYC timezone
#eastern = pytz.timezone("US/Eastern")
#localized_pickup_datetime = eastern.localize(date, is_dst=None)

# convert the user datetime to UTC and format the datetime as expected by the pipeline
#utc_pickup_datetime = localized_pickup_datetime.astimezone(pytz.utc)
#formatted_pickup_datetime = utc_pickup_datetime.strftime("%Y-%m-%d %H:%M:%S UTC")

params = dict(
    key=[key],  # useless but the pipeline requires it
    pickup_datetime=[key],
    pickup_longitude=[pickup_longitude],
    pickup_latitude=[pickup_latitude],
    dropoff_longitude=[dropoff_longitude],
    dropoff_latitude=[dropoff_latitude],
    passenger_count=[passenger_count])


response = requests.get(url, params=params)
data = response.json()
st.write(data)

df = pd.DataFrame({
    'latitude': pickup_latitude,
    'longitude': pickup_longitude,
    'name': ['SF', 'SF', 'SF']
})
st.map(df)
