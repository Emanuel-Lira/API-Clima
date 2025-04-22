from functions import *

if __name__ == '__main__':
  city = input('Digite o nome da cidade: ')
  print(f'Temperatura da cidade: {get_weather_temp(city)}C')
  print(f'Clima da cidade: {get_weather_main(city)}')