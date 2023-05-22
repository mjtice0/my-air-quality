import requests
import os 
from dotenv import load_dotenv


#load env variables from dotenv
load_dotenv()

# This function will be used to collect data for a specific and public PurpleAir sensor.
def getSensorData(sensor_index):

    # my_url is assigned the URL we are going to send our request to.
    my_url = 'https://api.purpleair.com/v1/sensors/' + str(sensor_index)

    # my_headers is assigned the context of our request we want to make. In this case
    # we will pass through our API read key using the variable created above.
    my_headers = {'X-API-Key':my_api_read_key}

    # This line creates and sends the request and then assigns its response to the
    # variable, r.
    r = requests.get(my_url, headers=my_headers)

    # We then return the response we received.
    return r