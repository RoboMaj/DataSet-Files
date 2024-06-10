import requests
import pandas as pd
from datetime import datetime

# Define the API endpoint and parameters
url = "https://rest.coinapi.io/v1/ohlcv/BITSTAMP_SPOT_ETH_USD/history"
headers = {'X-CoinAPI-Key' : 'C7F3BD0C-F269-4443-A06A-C6E0A9B19A10'}
params = {
    'period_id': '5MIN',
    'time_start': datetime(2022, 11, 1).isoformat(),
    'time_end': datetime(2022, 12, 31).isoformat()
}

# Send a GET request to the API
response = requests.get(url, headers=headers, params=params)

# Parse the response and convert it into a pandas DataFrame
data = response.json()
df = pd.DataFrame(data)
print(df.head())
print(df.shape[1])
print(df.columns)
# Rename the columns of the DataFrame
#df.columns = ['Open time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close time', 'Quote asset volume', 'Number of trades', 'Taker buy base asset volume', 'Taker buy quote asset volume']

# Convert the timestamp columns to a readable format
df['Open time'] = pd.to_datetime(df['time_period_start'])
df['Close time'] = pd.to_datetime(df['time_period_end'])

# Drop the unnecessary columns
df = df.drop(columns=['time_period_start', 'time_period_end'])

# Save the DataFrame to a CSV file
df.to_csv('ETH_data.csv', index=False)