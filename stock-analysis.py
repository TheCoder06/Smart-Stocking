import requests
import argparse
import json
from iexfinance.stocks import Stock


argparser = argparse.ArgumentParser()
argparser.add_argument('ticker',help = '')
args = argparser.parse_args()
ticker = args.ticker

#print (ticker)

book_url = "https://api.iextrading.com/1.0/stock/%s/book"%(ticker)


book_response = requests.get(book_url)

book_data = json.loads(book_response.content)

open = book_data['quote']['open']

print ("Opening Price:%s"%open)

print ("")

stats_url = "https://api.iextrading.com/1.0/stock/%s/stats"%(ticker)


stats_response = requests.get(stats_url)

stats_data = json.loads(stats_response.content)  
#print (data)

returnOnEquity = stats_data['returnOnEquity']

EPSSurprisePercent = stats_data['EPSSurprisePercent']

beta = stats_data['beta']

profitMargin = stats_data["profitMargin"]

returnOnAssets = stats_data["returnOnAssets"]

dividendYield = stats_data["dividendYield"]

priceToSales = stats_data["priceToSales"]

print ("Price to Sales Ratio:%s"%priceToSales)
print ("")
print ("Dividend Yield:%s"%dividendYield)
print ("")
print ("Return on Assets,(ROA):%s"%returnOnAssets)
print ("")
print ("Profit Margin:%s"%profitMargin)
print ("")
print ("Return On Equity:%s"%returnOnEquity)
print ("")
print ("EPS Suprise Percent:%s"%EPSSurprisePercent)
print ("")
print ("Beta:%s"%beta)

print ("")
print ("")

if dividendYield == 0:
    print ("This stock doesn't pay out a Dividend.")

if dividendYield < 1.99:
    print ("This stock's Dividend Yield is not good")


if dividendYield > 1.99:
    print ("This stock's Dividend Yield is good")

print ("")

if returnOnAssets > 5:
    print ("This stock's Return on Assets,(ROA), is good")
else:
    print ("This stock's Return on Assets,(ROA), is not good")

print ("")

if profitMargin > 11.6:
    print ("This stock's Profit Margin is good")
else:
    print ("This stock's Profit Margin is not good")

print ("")

if returnOnEquity > 18:
    print ("This stock's ROE,(Return On Equity) is good")
else:
    print ("This stock's ROE,(Return On Equity)is not good")

print ("")

if EPSSurprisePercent > 10:
    print ("This stock's earning suprise % is good")
else:
    print ("This stock's earning suprise % is not good")

print ("")

if beta < 1:
    print ("This stock is less risky than the overall stock market but may have a lower return")

if beta > 1:
    print("This stock is more risky than the overall stock market but may have the potential for higer returns")
