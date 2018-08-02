#This code connects to the Binance exchange and fetches the exchange rates of some of the cryptocurrencies 1 minute prior to run.
import datetime
from time import sleep
from binance.client import Client
client = Client('api key','api secret')
exchange_rates =[]     #This is used to store the rates
symbols = ['BTCUSDT','ETHUSDT','BNBUSDT','BCCUSDT','ADAUSDT','NEOUSDT','LTCUSDT','XRPUSDT','QTUMUSDT']




try:
# starting a loop to pick the symbols from the symbols list and getting their rates and printing them out
   print 'The Exchange Rates of some of the cryptocurrencies 1 minute ago in USD were: \n'
   for n in symbols:
        price = client.get_historical_klines(symbol = n,interval = '1m',start_str ='1 minutes ago UTC')
        print n, price[0][4]
        exchange_rates.append(price[0][4])
except IndexError:
    print 'Sorry, unable to fetch results, Please try again later'


sleep(2)