from flask import Flask, render_template, request
import requests
import os 
from dotenv import load_dotenv
import schedule
import time
from send_sms import * 

load_dotenv()

app = Flask(__name__)

# Api key variables
my_api_read_key = os.getenv("API_READ_KEY")
my_api_write_key = os.getenv("API_WRITE_KEY")

@app.route("/")
def home():
    return '<h1>Hello, Air Quality</h1>'

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        phone = request.form['phone']
        aqi_threshold = request.form['aqi_threshold']

        return "Registration successful!"

    return render_template("registration.html")

@app.route("/search")
def search():
    my_url = "https://api.purpleair.com/v1/sensors/168067"
    my_headers = {'X-API-Key':my_api_read_key}
    response = requests.get(my_url, headers= my_headers)
    purple_air_data = response.json()
    result = purple_air_data['sensor']['pm2.5']
    print("API call executed")
    aqi = convert_to_AQI(result)
    send_alert(aqi)
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

def send_alert(aqi):
    if aqi > 0:
        send_sms(aqi)


def API_call_schedule():
    def scheduled_call():
        API_response = search()

        aqi = convert_to_AQI(API_response)
        
        send_alert(aqi)

        # save_to_database(aqi)

    schedule.every(10).seconds.do(scheduled_call)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    app.run()


# # Add logic to check if aqi value is the same as the previous value, if it is, don't send alert
# # Can update sms send logic to send message based on aqi level -- if aqi < 50, sms = air quality is good
# # Will need to add error logic for sequence of function calls so program does not break

