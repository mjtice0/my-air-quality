import requests
import os 
from dotenv import load_dotenv

# Load env variables from dotenv
load_dotenv()

# My api key variables
my_api_read_key = os.getenv("API_READ_KEY")
my_api_write_key = os.getenv("API_WRITE_KEY")

    # my_url is the sensor where I'm getting information 
my_url = "https://api.purpleair.com/v1/sensors/121321"

    # my_headers is assigned the context of our request we want to make. 
my_headers = {'X-API-Key':my_api_read_key}

    # This line creates and sends the request and then assigns its response to the response variable
response = requests.get(my_url, headers=my_headers)
    #  Get data in json format
purple_air_data = response.json()
    # Extract desired values for calculating aqi
pm25 = purple_air_data['sensor']['pm2.5']
pm25_average = purple_air_data['sensor']['stats_b']['pm2.5_10minute']
print(pm25)
print(pm25_average)

# Function to convert pm2.5 to US aqi
# Formula:
# Cp = the truncated concentration of pollutant p
# BPHi = the concentration breakpoint that is greater than or equal to Cp 
# BPLo = the concentration breakpoint that is less than or equal to Cp
# IHi = the AQI value corresponding to BPHi
# ILo = the AQI value corresponding to BPLo

# def calculate_AQI(Cp, Ih, Il, BPh, BPL):
#     12.1 - 35.4
# 150 - 101 (pm2.5 - 12.1) + 101
# 35.4 - 12.1
#     a = (Ih - Il)
#     b = (BPh - BPl)
#     c = (Cp - BPL)


# Function to send get request at intervals -- Data is updated every two minutes