import os
import json
from dotenv import load_dotenv
import requests
import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")

load_dotenv()
api_key=os.getenv('API_KEY')
city=input("Enter the name of the city: ")
url=f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city.lower().strip()}"

r=requests.get(url)
dic=json.loads(r.text)

print()
speak.Speak(f"The temperature in {city} is {dic['current']['temp_c']} degree celsius")
print(f"Area: {dic['location']['name']}\n")
print(f"Temperature in *C: {dic['current']['temp_c']}")
print(f"Temperature in *F: {dic['current']['temp_f']}")
print(f"Wing speed (in Kmph): {dic['current']['wind_kph']}")