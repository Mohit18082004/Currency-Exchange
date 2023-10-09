# Function to fetch exchange rates from the API
def get_exchange_rates(base_currency):
    params = {"base": base_currency}
    response = requests.get(API_URL, params=params)
    data = response.json()
    return data.get("rates", {})

# Function to monitor exchange rates and send alerts
def monitor_exchange_rates(base_currency, foreign_currencies, thresholds):
    while True:
        rates = get_exchange_rates(base_currency)
        for foreign_currency, threshold in thresholds.items():
            if foreign_currency in rates:
                rate = rates[foreign_currency]
                if rate > threshold['upper'] or rate < threshold['lower']:
                    print(f"Alert: {base_currency} to {foreign_currency} rate crossed the threshold!")
                    print(f"Current Rate: {rate}")
                    print(f"Threshold: Upper={threshold['upper']}, Lower={threshold['lower']}")
        time.sleep(60)  # Check rates every 60 seconds

if _name_ == "_main_":
    base_currency = input("Enter your base currency (e.g., USD): ")
    num_currencies = int(input("Enter the number of foreign currencies to monitor: "))
    
    foreign_currencies = []
    thresholds = {}
    
    for _ in range(num_currencies):
        foreign_currency = input("Enter the foreign currency (e.g., INR): ")
        upper_threshold = float(input(f"Enter the upper threshold for {foreign_currency}: "))
        lower_threshold = float(input(f"Enter the lower threshold for {foreign_currency}: "))
        
        foreign_currencies.append(foreign_currency)
        thresholds[foreign_currency] = {"upper": upper_threshold, "lower": lower_threshold}
    
    print("\nMonitoring exchange rates...")
    monitor_exchange_rates(base_currency, foreign_currencies, thresholds
