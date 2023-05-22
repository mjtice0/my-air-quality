import requests
import os 
from dotenv import load_dotenv

# Load env variables from dotenv
load_dotenv()

# My api key variables
my_api_read_key = os.getenv("API_READ_KEY")
my_api_write_key = os.getenv("API_WRITE_KEY")


def call_API():
    my_url = "https://api.purpleair.com/v1/sensors/121321"
    my_headers = {'X-API-Key':my_api_read_key}
    response = requests.get(my_url, headers=my_headers)
    purple_air_data = response.json()
    result = purple_air_data['sensor']['pm2.5']
    
    return result
# Function to convert pm25 raw number to AQI, calls calculate AQI function
def convert_to_AQI(result):
    pm25 = result

    if pm25 < 0:
        return pm25
    
    if pm25 > 250.5:
        return calculate_AQI(pm25, 500, 301, 500.4, 250.5)
    elif pm25 > 150.5:
        return calculate_AQI(pm25, 300, 201, 250.4, 150.5)
    elif pm25 > 55.5:
        return calculate_AQI(pm25, 200, 151, 150.4, 55.5)
    elif pm25 > 35.5:
        return calculate_AQI(pm25, 150, 101, 55.4, 35.5)
    elif pm25 > 12.1:
        return calculate_AQI(pm25, 100, 51, 35.4, 12.1)
    elif pm25 >= 0:
        return calculate_AQI(pm25, 50, 0, 12, 0)
    else:
        return None

# Formula to convert PM to AQI from Airnow.gov:
# Cp = the truncated concentration of pollutant p
# BPHi = the concentration breakpoint that is greater than or equal to Cp 
# BPLo = the concentration breakpoint that is less than or equal to Cp
# IHi = the AQI value corresponding to BPHi
# ILo = the AQI value corresponding to BPLo

# Function to calculate pm2.5 to US aqi
def calculate_AQI(Cp, IHi, ILo, BPHi, BPLo):
    a = (IHi - ILo)
    b = (BPHi - BPLo)
    c = (Cp - BPLo)
    return round((a / b) * c + ILo)

API_response = call_API()
print(convert_to_AQI(API_response))

# Function to send get request at intervals -- Data is updated every two minutes
# def get_data(takes_in_request_function):
    # If countdown === 10 min:
    # Retrieve data
    # Store Data in DB? 
# Function to determine if AQI is over a certain amount
 # If # > 80, send messeage

  # pm25_average = purple_air_data['sensor']['stats_b']['pm2.5_10minute']