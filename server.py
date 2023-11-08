import requests
from flask import Flask, request, jsonify

# Create Flask application
app = Flask(__name__)

#  Initialize variable for Weather.gov API
API_BASE_URL = 'https://api.weather.gov'


@app.route('/get-weather')
def get_weather():
    # https://api.weather.gov/points/{latitude},{longitude}
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')

    if not latitude or not longitude:
        return jsonify({'Error': 'Latitude and longitude are required parameters'}), 400
    
    endpoint_url = f'{API_BASE_URL}/points/{latitude},{longitude}'
    weather_data = call_api(endpoint_url)

    if not weather_data:
        return jsonify({'Error': 'Failed to retrieve weather data.'}), 500
    
    forecast_url = weather_data['properties']['forecast']
    forecast = get_forecast(forecast_url)

    if not forecast:
        return jsonify({'Error': 'Failed to retrieve weather data.'}), 500
    
    return jsonify(forecast)


def call_api(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except:
        return None
    return None


def get_forecast(url):
    forecast_data = call_api(url)

    if forecast_data:
        periods = forecast_data['properties']['periods']
        weather = []

        for period in periods:
            data = {
                'day': period.get('name'),
                'temperature': period.get('temperature'),
                'forecast': period.get('shortForecast')
            }
            weather.append(data)

        return weather

    else:
        return None


if __name__ == '__main__':
    app.run(debug=True)

