from urllib.request import Request, urlopen
from urllib.error import URLError
import json

# HTTP GET
someurl = 'https://cloud.iexapis.com/stable/tops?token=YOUR_API_TOKEN_HERE&symbols=aapl'
req = Request(someurl)

try:
    response = urlopen(req)
except URLError as e:
    if hasattr(e, 'reason'):
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    elif hasattr(e, 'code'):
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
else:
    data = response.read().decode('utf-8')
    data_array = json.loads(data)
    data_dict = data_array[0]
    print(f"{data_dict['symbol']}, {data_dict['lastSalePrice']}, {data_dict['sector']}")