import requests 

api_key = "9e3580d9a56308293d1acdb060401334"

user_input = input("Enter a  city: ")

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")
cloud = weather_data.json()['weather'][0]['main']
temp = weather_data.json()['main']['temp']
temp_c = 5/9 * (temp - 32)

print(f"The weather in the {user_input} is {cloud}")
print(f"The Temperature in the {user_input} is {temp}°F")
print(f"The temperature in celsius:{temp_c:.2f}°C")
