"""Grabs all cross currency pairs from Yahoo! Finance
this requires the ystockqutoe module"""

from ystockquote import get_price
import csv

ccyList = [
    'GBP' ,'USD' ,'EUR' ,'ALL' ,'AOA' ,'ARS' ,'AUD' ,'BHD' ,'BDT','BYR' ,'BGN' ,'BOB' ,'BRL' ,'BND' ,'CAD' ,'CLP'
    ,'CNY' ,'COP' ,'CDF' ,'CRC' ,'HRK','CZK','DKK','EGP','FJD','HKD','HUF','ISK' ,'INR','IDR','ILS' ,'JPY','KRW','KWD',
    'LVL' ,'LTL' ,'MYR' ,'MXN' ,'NZD' ,'NOK' ,'PKR' ,'PHP' ,'PLN' ,'RUB' ,'SAR' ,'SGD' ,'ZAR' ,'SEK' ,'CHF' ,'THB'
    ,'TRY','AED' ,'TWD' ,'UAH'
]

allPairs = []
pairPrice  = {}

for ccy1 in ccyList:
    for ccy2 in ccyList:
        if ccy1 == ccy2:
            pass
        else: allPairs.append(ccy1+ccy2)


for pair in allPairs:
    price = get_price(str(pair) + '=X')
    pairPrice[pair] = price

    with open('prices.csv', 'w') as f:
        w = csv.DictWriter(f, pairPrice.keys())
        w.writeheader()
        w.writerow(pairPrice)