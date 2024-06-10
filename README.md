This Python script fetches historical OHLCV (Open, High, Low, Close, Volume) data for Bitcoin (BTC) against the US Dollar (USD) from CoinAPI and saves it to a CSV file named "bitcoin_data.csv".

Requirements:

Python 3.x
requests library (pip install requests)
pandas library (pip install pandas)
Instructions:

1.  Replace 'C7F3BD0C-F269-4443-A06A-C6E0A9B19A10' with your own CoinAPI API key in the headers dictionary. You can obtain a free API key by creating an account on CoinAPI https://docs.coinapi.io/.
2.  Run the script using python script_name.py. This will download data for the period between November 1st, 2022 and December 31st, 2022 with a 5-minute time interval.
You can modify the params dictionary to change the:
period_id: Time interval between data points (e.g., '1HRS', '1DAY')
time_start: Start date of the data retrieval (YYYY-MM-DD format)
time_end: End date of the data retrieval (YYYY-MM-DD format)
Output:

The script will print:

3.  The **first** 5 rows of the downloaded data (df.head())
4.  The number of columns in the data (df.shape[1])
5.  The column names (df.columns)
The script will also save the complete data as a CSV file named "bitcoin_data.csv".
