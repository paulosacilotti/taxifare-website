import streamlit as st
import datetime
import requests
import pandas as pd
import json
import pytz
from datetime import datetime

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''


default_latitude = 40.730610
default_longitude = -73.935242

pickup_longitude = st.number_input("Pick up longitude:", value=default_longitude)
pickup_latitude = st.number_input("Pick up latitude:", value=default_latitude)
dropoff_longitude = st.number_input("Drop off longitude:", value=default_longitude)
dropoff_latitude = st.number_input("Drop off latitude:", value=default_latitude)

passenger_count = st.number_input("number of passengers", value=1)
'''

## Once we have these, let's call our API in order to retrieve a prediction
S
See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''


url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
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
