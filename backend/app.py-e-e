from flask import Flask
import requests
import os 
from dotenv import load_dotenv
import schedule
import time
from send_sms import * 

app = Flask(__name__)
load_dotenv()

# Api key variables
my_api_read_key = os.getenv("API_READ_KEY")
my_api_write_key = os.getenv("API_WRITE_KEY")

@app.route("/")
def home():
    return '<h1>Hello, World</h1>'

@app.route("/search")
def search():
    my_url = "https://api.purpleair.com/v1/sensors/121321"
    my_headers = {'X-API-Key':my_api_read_key}
    response = requests.get(my_url, headers=my_headers)
    purple_air_data = response.json()
    result = purple_air_data['sensor']['pm2.5']
    print("API call executed")
    aqi = convert_to_AQI(result)
    return f"The AQI for your location is: {aqi}"

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

# Function to calculate pm2.5 to US aqi
def calculate_AQI(Cp, IHi, ILo, BPHi, BPLo):
    a = (IHi - ILo)
    b = (BPHi - BPLo)
    c = (Cp - BPLo)
    aqi = round(((a / b) * c + ILo))
    print("Calculation executed")
    return aqi


if __name__ == '__main__':
    app.run()
    search()
    

# # Function to make API call to get sensor data 
# def call_API():
    # my_url = "https://api.purpleair.com/v1/sensors/121321"
    # my_headers = {'X-API-Key':my_api_read_key}
    # response = requests.get(my_url, headers=my_headers)
    # purple_air_data = response.json()
    # result = purple_air_data['sensor']['pm2.5']
    # print("API call executed")
    # return result
# # Function to convert pm25 raw number to AQI, calls calculate AQI function
# def convert_to_AQI(result):
#     pm25 = result

#     if pm25 < 0:
#         return pm25
    
#     if pm25 > 250.5:
#         return calculate_AQI(pm25, 500, 301, 500.4, 250.5)
#     elif pm25 > 150.5:
#         return calculate_AQI(pm25, 300, 201, 250.4, 150.5)
#     elif pm25 > 55.5:
#         return calculate_AQI(pm25, 200, 151, 150.4, 55.5)
#     elif pm25 > 35.5:
#         return calculate_AQI(pm25, 150, 101, 55.4, 35.5)
#     elif pm25 > 12.1:
#         return calculate_AQI(pm25, 100, 51, 35.4, 12.1)
#     elif pm25 >= 0:
#         return calculate_AQI(pm25, 50, 0, 12, 0)
#     else:
#         return None

# # Function to calculate pm2.5 to US aqi
# def calculate_AQI(Cp, IHi, ILo, BPHi, BPLo):
#     a = (IHi - ILo)
#     b = (BPHi - BPLo)
#     c = (Cp - BPLo)
#     aqi = round(((a / b) * c + ILo))
#     print("Calculation executed")
#     return aqi

# # Function to initiate sms text alert
# # Calls send_sms function
# def send_alert(aqi):
#     if aqi > 100:
#         send_sms(aqi)

# air_quality_list = []
# # Function to add data to database -- will be updated to work with db
# def save_to_database(aqi):
#     air_quality_list.append(aqi)

#     print(air_quality_list)

# # Function to send get request at intervals -- Data is updated every two minutes, retrieve data every hour
# # Currently on 10s schedule for testing 
# # Change order of logic, call API_call_schedule in call_API function instead
# def API_call_schedule():
#     def scheduled_call():
#         API_response = call_API()

#         aqi = convert_to_AQI(API_response)
        
#         send_alert(aqi)

#         save_to_database(aqi)

#     schedule.every(10).seconds.do(scheduled_call)

#     while True:
#         schedule.run_pending()
#         time.sleep(1)

# API_call_schedule()


# # Add logic to check if aqi value is the same as the previous value, if it is, don't send alert
# # Can update sms send logic to send message based on aqi level -- if aqi < 50, sms = air quality is good
# # Will need to add error logic for sequence of function calls so program does not break

# # Things to consider:
# # - how long will intervals go
# # - memoize data
# # - how event is triggered by user

# # Formula to convert PM to AQI from Airnow.gov:
# # Cp = the truncated concentration of pollutant p
# # BPHi = the concentration breakpoint that is greater than or equal to Cp 
# # BPLo = the concentration breakpoint that is less than or equal to Cp
# # IHi = the AQI value corresponding to BPHi
# # ILo = the AQI value corresponding to BPLo