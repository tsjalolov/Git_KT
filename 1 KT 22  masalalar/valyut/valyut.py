from os import error

import requests  #pip install requests
data = requests.get(f'https://www.cbr-xml-daily.ru/daily_json.js').json()
print(data['Date'])
#print(data.keys())
#print(data['Valute'].keys())
for i in data['Valute']:
	print(i, '-->',data['Valute'][i]['Name'])


