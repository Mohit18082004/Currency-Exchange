# Currency-Exchange
Step1-install forex-python to get real time currency rates
Step2-open terminal and type pip-install
Forex python
Step3-Conversion into 8 lines of currency rate

from forex_python.converter import currencyRates
currency=CurrencyRates
amount=int(input("Enter amount:"))
from_curr=input("From Currency:").upper()
to_curr=input("To Currency:").upper()
print(from_curr,"To",to_curr,amt)
result =currency.convert(from_curr,to_curr,amt)
print(Conversion Amount:",result)
a)
For a trade to occur, one currency must be exchanged for another. To buy British Pounds (GBP), another currency must be used to buy it. Whatever currency is used will create a currency pair. If U.S. dollars (USD) are used to buy GBP, the exchange rate is for the GBP/USD pair. Access to these forex (foreign exchange) markets can be found through any of the major forex brokers.
Base currency (also called transaction currency) is always given first in a currency pair; quote currency (also called counter currency) is given second.
b) currency exchange API to real time
Exchange rates:-
 import requests
from datetime import datetime 

class Currency:
    def_init_(self):
        self.api_key=open('api_key').readline().strip()
        self.url=f'http://api.exchangeratesapi.i0/v1/latest?access_key(self.api_key}'
        self.output=' '
        self.file.name=datetime.now().strftime('%d %b -%Y')
        
        def do_request(self):
            res=requests.get(self.url)
            if res.status_code=200:
                self.output=res.json()
                
                
                def write_to_file(self):
                    print (self.output['rates'] ['USD'])
                    
                    
               c=Currency()
               c.do_request()
               c.write_to_file()
d)
In[1]:mport numpy as np
import pandas as pd
In[2]: import matplotlib.pyplot as plt
import seaborn as sns
In[3]: from seaborn import regression
In[4]:sns.set()
In[5]:plt.style.use('seaborn-whitegrid')
In[6]: data=pd.read_csv("Download.csv")
In[7]:data
In[9]:plt.figure(figsize=(10,4))
plt.title("INR - USD Exchange rate")
plt.xlabel("Date")
plt.ylabel("Close")
plt.plot(data["Close"])
plt.show()
In[10]:x=data["Open","High","Low"]]
y=data["Close"]
x=x.to_numpy()
y=y.to_numpy()
y=y.reshape(-1,1)
In[11]: from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytrest=train_test_split(x,y, test_size=0.2, random_state=42)

In[12]: from sklearn.tree import DecisionTreeRegressor
model=DecisionTreeRegressor()
model.fit(xtrain, ytrain)
