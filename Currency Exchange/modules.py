import uAgent
import requests
import time
base_currency = input("Enter your base currency: ")
foreign_currencies = input("Enter the foreign currencies you want to monitor (comma-separated): ").split(',')
thresholds = {}

for currency in foreign_currencies:
    lower_threshold = float(input(f"Enter lower threshold for {currency}: "))
    upper_threshold = float(input(f"Enter upper threshold for {currency}: "))
    thresholds[currency] = (lower_threshold, upper_threshold)
