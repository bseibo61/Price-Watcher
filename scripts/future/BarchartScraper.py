import config
from zeep import Client
# ondemand = Client('https://ondemand.websol.barchart.com/service?wsdl')

# result = client.service.getHistory('YOUR_API_KEY', 'AAPL', 'minutes', '20100101', '20130101', '10', '60', 'asc', 'EFK', 'true', 'true', 'sum', '1', 'true', 'NYSE,AMEX,NASDAQ', 'false', '1', 'expiration')

# print(result)

client = Client('https://ondemand.websol.barchart.com/service?wsdl')

result = client.service.getHistory(config.BarchartApiKey, 'AAPL', 'minutes', '20100101', '20130101', '10', '60', 'asc', 'EFK', 'true', 'true', 'sum', '1', 'true', 'NYSE,AMEX,NASDAQ', 'false', '1', 'expiration')

# print(result)