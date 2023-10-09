def fetch_exchange_rates():
    api_key = 'YOUR_API_KEY'
    base_url = f'https://api.openexchangerates.org/latest?base={base_currency}&apikey={api_key}'
    response = requests.get(base_url)
    data = response.json()
    return data['rates']
