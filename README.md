# 🌤 Weather Microservice
This microservice provides weather information based on latitude and longitude coordinates using the National Weather Service (NSW) API.

# 📮 How to Request and Receive Data

### API Endpoint
- Base URL: `https://microservice-weather-67ea12ff0a34.herokuapp.com`
- Endpoint: `/get-weather`
- Parameters:
  - `latitude`: Latitude coordinate (e.g., 47.6062)
  - `longitude`: Longitude coordinate (e.g., -122.3321)
 
### Sample Request 1
```
curl https://microservice-weather-67ea12ff0a34.herokuapp.com/get-weather?latitude=47.6062&longitude=-122.3321
```

### Sample Request 2
```
# Python3
import requests

# Define the API endpoints and params
base_url = "https://microservice-weather-67ea12ff0a34.herokuapp.com"
endpoint = "/get-weather"
latitude = 47.6062
longitude = -122.3321

# Construct API request URL
url = f'{base_url}{endpoint}?latitude={latitude}&longitude={longitude}'

# Send the GET request
response = requests.get(url)

# Parse the response if successful
if response.status_code == 200:
  weather_data = response.json()
else:
  print(f'Error: {response.status_code}')
```

### Response
- The response is expected in JSON format, representing a list of dictionaries.
- Each dictionary contains key-value pairs for the following:
  - `day`: Day of the forecast (e.g., 'Today')
  - `forecast`: Short weather forecast description (e.g., 'Mostly Sunny')
  - `temperature`: Temperature in degrees Farenheight (e.g., 65)
- Example
  ```
  [
    {
      "day":"Today",
      "forecast":"Partly Sunny",
      "temperature":48
    },
    {
      "day":"Tonight",
      "forecast":"Mostly Cloudy",
      "temperature":42
    },
    # ...more data for other days
  ]
  ```

### UML Sequence Diagram
![Screenshot 2023-11-20 at 9 25 26 AM](https://github.com/ahleeneh/weather-microservice/assets/107948221/f758da79-bd6f-4b69-ae70-34dbe7982e51)
