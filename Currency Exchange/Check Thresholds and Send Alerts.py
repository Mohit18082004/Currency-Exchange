def send_alert(currency, rate):
    lower_threshold, upper_threshold = thresholds[currency]
    if rate < lower_threshold or rate > upper_threshold:
        uAgent.send_alert(f"Alert: {base_currency}/{currency} rate is {rate}")
