import json
from pprint import pprint

with open('result.json') as f:
    data = json.load(f)

tickers = {"AMD": {}, "TLRY": {}, "MU": {}, "BABA": {}, "IQ": {}, "JD": {}, "TCEHY": {}, "APRN": {}}

print("data length is",len(data))

for date in data:
    for ticker in data[date]:
        innerDict = {date: data[date][ticker]}
        tickers[ticker][date] = data[date][ticker]
        print(ticker)

pprint(tickers)

with open('Revisedresult.json','w') as fp:
		json.dump(tickers,fp)