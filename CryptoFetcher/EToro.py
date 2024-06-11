import requests
from pprint import pprint
import json

# Replace "BTC" with the symbol of the cryptocurrency you want to fetch data for
symbol = "BTC"

url = f"https://candle.etoro.com/candles/asc.json/FiveMinutes/2/{symbol}"

response = requests.get(url)

if response.status_code != 200:
    print(f"Error: {response.status_code} -> {response.text}")
else:
    data = response.json()

    with open("test.json", "w") as f:
        json.dump(data, f, indent=4)
    pprint(data)
