# Weather Forecasting Tool - Create a command line tool that accepts a city's name and returns the 
# current weather forecast.
# The tool should display the current weather conditions (e.g. cloudy, sunny, rain, etc.) along 
# with the temperature in Fahrenheit.
# The tool should also display the 5-day forecast including the minimum and maximum temperatures 
# for each day.
# The tool should leverage the OpenWeatherMap API to fetch weather data and parse it using Python.
# The tool should be able to handle invalid inputs and display a message to the user indicating the 
# error.

# helper function to make api call, parse response and display weather forecast

def make_api_call(complete_url, is_first_call):
    # Importing the requests library
    import requests
    # get method of requests module return response object
    response = requests.get(complete_url)

    # json method of response object convert json format data into python format data
    response_json = response.json()

    # check the value of "cod" key is equal to "404", means city is found otherwise, city is not 
    # found
    return_code = response_json["cod"]
    if return_code == "200":
        if is_first_call:
            print (response_json)
            print ("Weather condition is ", response_json.weather[0].description)
            print ("Temperature in Fahrenheit is ", response_json.main.temp)
            # Get 5 day forecast
            # base_url variable to store url
            base_url = "http://api.openweathermap.org/data/2.5/forecast?"
            complete_url = base_url + "appid=" + api_key + "&lat=" + str(response_json.coord.lat) \
                + "&lon=" + str(response_json.coord.lon)
            make_api_call(complete_url, False)
        else:
            # iterate through 5 day forecast
            for i in range(0, 40, 8):
                print ("Date: ", response_json.list[i].dt_txt)
                print ("Weather condition is ", response_json.list[i].weather[0].description)
                print ("Minimum temperature in Fahrenheit is ", response_json.list[i].main.temp_min)
                print ("Maximum temperature in Fahrenheit is ", response_json.list[i].main.temp_max)
                print ("")
    else:
        if return_code == "404":
            if is_first_call:
                print ("ERROR: City Not Found")
            else:
                print ("ERROR: Location Not Found")
        else:
            print ("ERROR: Received HTTP Status Code ", return_code, " from API")        

# main function to forecast weather

def forecast_weather(city_name):
    # Importing the os library
    import os

    # API key
    api_key = os.environ.get('OPEN_WEATHER_MAP_API_KEY')

    # base_url variable to store url
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    # complete_url variable to store complete url address
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    make_api_call(complete_url, True)
    
# Driver program
if __name__ == "__main__":
    city_name = input("Enter city name : ")
    forecast_weather(city_name)

# Sample Output:
# Enter city name : New York
# Weather condition is  overcast clouds
# Temperature in Fahrenheit is  283.15
# Date:  2019-11-21 18:00:00
# Weather condition is  overcast clouds
# Minimum temperature in Fahrenheit is  282.15
# Maximum temperature in Fahrenheit is  283.15

# unittest
# import unittest
# class TestForecastWeather(unittest.TestCase):
#     def test_forecast_weather(self):
#         self.assertEqual(forecast_weather("New York"), "Weather condition is  overcast clouds")

# References:
# https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/
# https://openweathermap.org/forecast5
# https://openweathermap.org/current

