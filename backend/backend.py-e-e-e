import requests
import os 
from dotenv import load_dotenv


# Load env variables from dotenv
load_dotenv()

my_api_read_key = os.getenv("API_READ_KEY")
my_api_write_key = os.getenv("API_WRITE_KEY")


# def getSensorData(sensor_index):

    # my_url is assigned the URL we are going to send our request to.
my_url = "https://api.purpleair.com/v1/sensors/121321"

    # my_headers is assigned the context of our request we want to make. In this case
    # we will pass through our API read key using the variable created above.
my_headers = {'X-API-Key':my_api_read_key}

    # This line creates and sends the request and then assigns its response to the
response = requests.get(my_url, headers=my_headers)
print(response.status_code)