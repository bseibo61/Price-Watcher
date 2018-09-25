import requests
import pprint
import json

pp = pprint.PrettyPrinter(indent=4)

ticker = "AAPL"
NumBullsih = 0
NumBearish = 0

r = requests.get("https://api.stocktwits.com/api/2/streams/symbol/"+ticker+".json")
print(r.status_code)
JsonResponse = r.json()
for post in JsonResponse['messages']:
    CurrSentiment = post['entities']['sentiment']
    if CurrSentiment != None:
        print(CurrSentiment)
        if CurrSentiment['basic'] == "Bullish":
            NumBullsih += 1
        elif CurrSentiment['basic'] == "Bearish":
            NumBearish += 1 
print(NumBullsih, "are bullsih and ", NumBearish, "are bearish")