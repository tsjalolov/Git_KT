
import requests
json = requests.get(f'https://www.cbr-xml-daily.ru/daily_json.js').json()

print('1-->', json)
print('2-->', json.keys())
print('3-->', json['Date'])
print('4-->', json['Valute'])
print('5-->', json['Valute'].keys())
print('6-->', json['Valute']['UZS']['Name'])
for i in json['Valute']:
    print(i, json['Valute'][i]['Name'])
