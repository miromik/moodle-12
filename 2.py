import requests

API_KEY = "683a3eb440ea9dd63b1e873b19634350"

city = input("Anna paikkakunnan nimi: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

response = requests.get(url)

if response.status_code == 200:
  data = response.json()

  temp_kelvin = data["main"]["temp"]
  temp_celsius = temp_kelvin - 273.15
  description = data["weather"][0]["description"]

  print(f"\nPaikkakunta: {city.capitalize()}")
  print(f"Säätila: {description}")
  print(f"Lämpötila: {temp_celsius:.1f} °C")
else:
  print("Virhe haettaessa säätietoja. Tarkista paikkakunnan nimi ja API-avain.")