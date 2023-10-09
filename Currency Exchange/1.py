while True:
    rates = fetch_exchange_rates()
    for currency in foreign_currencies:
        rate = rates[currency]
        send_alert(currency, rate)
    time.sleep(300)  # Delay for 5 minutes before checking again (adjust as needed)
