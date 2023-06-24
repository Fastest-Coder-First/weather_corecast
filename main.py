# Weather Forecasting Tool - Create a command line tool that accepts a city's name and returns the current weather forecast.
# The tool should display the current weather conditions (e.g. cloudy, sunny, rain, etc.) along with the temperature in Fahrenheit.
# The tool should also display the 5-day forecast including the minimum and maximum temperatures for each day.
# The tool should leverage the OpenWeatherMap API to fetch weather data and parse it using Python.
# The tool should be able to handle invalid inputs and display a message to the user indicating the error.

def forecast_weather(city_name):
    # Importing the requests library
    import requests

    # API key
    api_key = "e8b0f1b0b0b0b0b0b0b0b0b0b0b0b0b0"

    # base_url variable to store url
    base_url = "http://api.openweathermap.org/data/2.5/current?"
    
    # complete_url variable to store complete url address
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    # get method of requests module return response object
    response = requests.get(complete_url)

    # json method of response object convert json format data into python format data
    response_json = response.json()

    # check the value of "cod" key is equal to "404", means city is found otherwise, city is not found
    if response_json["cod"] != "404":
        print ("Weather condition is ", response_json.weather[0].description)
        print ("Temperature in Fahrenheit is ", response_json.main.temp)
        # Get 5 day forecast
        # base_url variable to store url
        base_url = "http://api.openweathermap.org/data/2.5/forecast?"
        complete_url = base_url + "appid=" + api_key + "&lat=" + str(response_json.coord.lat) + "&lon=" + str(response_json.coord.lon)
        # get method of requests module return response object
        response = requests.get(complete_url)
        # json method of response object convert json format data into python format data
        response_json = response.json()
        # check the value of "cod" key is equal to "404", means city is found otherwise, city is not found
        if response_json["cod"] != "404":
            # iterate through 5 day forecast
            for i in range(0, 40, 8):
                print ("Date: ", response_json.list[i].dt_txt)
                print ("Weather condition is ", response_json.list[i].weather[0].description)
                print ("Minimum temperature in Fahrenheit is ", response_json.list[i].main.temp_min)
                print ("Maximum temperature in Fahrenheit is ", response_json.list[i].main.temp_max)
                print ("")
        else:
            print ("ERROR: City Not Found")
    else:
        print ("ERROR: City Not Found")

    
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
