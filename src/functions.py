import requests
from dotenv import load_dotenv
import os

load_dotenv()  # Carrega variáveis do .env

api_key = os.getenv("API_KEY")

#  appid={API key}&q={city}

# response = requests.get(complete_url)
# print(response.json()['weather'])

def get_weather_API(city):
  try:
    base_url = 'https://api.openweathermap.org/data/2.5/weather?'
    complete_url = f'{base_url}appid={api_key}&q={city}'
    response = requests.get(complete_url)
    data = response.json()

    if response.status_code == 200:
            return data
    else:
            return None
    
  except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar à API: {e}")
        return None

def get_weather_temp(city):
  response = get_weather_API(city)
  if not response:  # Ou if response is None
        return None
  temp = response['main']['temp']
  return round((temp - 273.15), 2)

def get_weather_main(city):
  response = get_weather_API(city)
  if not response:
        return None
  return  response['weather'][0]['main']
  
