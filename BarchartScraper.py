import requests
import pprint
import json
import config



r = requests.get("https://api.stocktwits.com/api/2/streams/symbol/"+ticker+".json")
print(r.status_code)


ondemand = Client('https://marketdata.websol.barchart.com/service?wsdl')

result = client.service.getQuote('YOUR_API_KEY', 'AAPL,GOOG', 'fiftyTwoWkHigh,fiftyTwoWkHighDate,fiftyTwoWkLow,fiftyTwoWkLowDate')

print(result)