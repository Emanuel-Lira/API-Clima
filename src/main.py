from functions import *


def entrada_valida(city):
    return city and not any(char.isdigit() for char in city)

if __name__ == '__main__':

 while True:   
  city = input('Digite o nome da cidade: ').strip()

  if not entrada_valida(city):
      
      print("⚠️ Entrada inválida. Digite um nome de cidade sem números e que não esteja vazio.")

  temp = get_weather_temp(city)
  clima = get_weather_main(city)

  if temp is None or clima is None:  
      print(f"Cidade '{city}' não encontrada")
      continue

    

  print(f'📍 Cidade consultada: {city}')
  print(f'🌡️ Temperatura da cidade: {get_weather_temp(city)} °C')
  print(f'🌦️  Clima da cidade: {get_weather_main(city)}')
  break
