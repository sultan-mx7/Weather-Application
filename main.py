import requests
API_KEY="1e4cae8d11eee8cbc981656eb9cdf1a1"
BASE_URL="https://api.openweathermap.org/data/2.5/weather"
City = input("Enter the name of the city: ")
request_url=f"{BASE_URL}?appid={API_KEY}&q={City}"
response=requests.get(request_url)
if response.status_code==200:
    data=response.json()
    name=data['name']
    country=data['sys']['country']
    weather=data['weather'][0]['description']
    temperature= round(data['main']['temp'],2)
    feels_like=data['main']['feels_like']
    pressure=data['main']['pressure']
    humidity=data['main']['humidity']
    print("City:",name)
    print("Country: ",country)
    print("Weather: ",weather)
    print("Temperature:",temperature)
    print("Feels Like : ",feels_like)
    print("pressure :",pressure)
    print("humidity : ",humidity)

else:
    print("An Error Occured")
    print("May be you have Entered Wrong City Name")
    # shortcut
    #     print("City:", data['name'])
    #     print("Country:", sys_data['country'])
    #     print("Weather:", weather_data['description'])
    #     print("Temperature:", round(main_data['temp'], 2))
    #     print("Feels Like:", main_data['feels_like'])
    #     print("Pressure:", main_data['pressure'])
    #     print("Humidity:", main_data['humidity'])

