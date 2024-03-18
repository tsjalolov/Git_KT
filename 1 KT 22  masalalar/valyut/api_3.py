
import requests
json = requests.get(f'https://www.cbr-xml-daily.ru/daily_json.js').json()
pul = float(input("rub kiriting -->"))
valyut = input("valyutani tanlang -->")
valyut = valyut.upper()
print('1-->', json)
print('2-->', json.keys())
print('3-->', json['Date'])
print('4-->', json['Valute'])
print('5-->', json['Valute'].keys())
print('6-->', json['Valute'][valyut]['CharCode'], json['Valute'][valyut]['Name'])
kurs_rubl = json['Valute'][valyut]['Nominal'] / json['Valute'][valyut]['Value']
print('7-->',pul,' rubl -->', round(pul * kurs_rubl, 2), valyut)
#for i in json['Valute']:
#    print(i, '-->',json['Valute'][i]['Value'], json['Valute'][i]['Name'])
