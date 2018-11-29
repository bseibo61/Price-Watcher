import json
from pprint import pprint

with open('result.json') as f:
    data = json.load(f)

tickers = {"AMD": {}, "TLRY": {}, "MU": {}, "BABA": {}, "IQ": {}, "JD": {}, "TCEHY": {}, "APRN": {}}

print("data length is",len(data))

for date in data:
    for ticker in data[date]:
        diff = (data[date][ticker][0] - data[date][ticker][1])/(data[date][ticker][1] + data[date][ticker][0])
        tickers[ticker][date] = diff
        print(ticker)

pprint(tickers)

with open('Revisedresult.json','w') as fp:
		json.dump(tickers,fp)