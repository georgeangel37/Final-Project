import pandas as pd
import requests

class Oanda:
   
    
    def __init__(self, base_currency, quote_currency, start_date, end_date):
        self.api_key = '484e889253109166172d86a73891234c-d787e35620f6145963e0d5b3ada0e91b'
        self.base_currency = base_currency
        self.quote_currency = quote_currency
        self.start_date = start_date
        self.end_date = end_date


    def create_data(self):
        url = f'https://api-fxpractice.oanda.com/v3/instruments/{self.base_currency}_{self.quote_currency}/candles'
        headers = {'Authorization': f'Bearer {self.api_key}'}
        params = {'granularity': 'D', 'from': self.start_date, 'to': self.end_date} 
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()['candles']
            df = pd.DataFrame(data)
            df.to_csv('forex_data.csv', index=False)
            print('Data exported to forex_data.csv successfully.')
        else:
            print('Failed to fetch data. Check your API key and parameters.')