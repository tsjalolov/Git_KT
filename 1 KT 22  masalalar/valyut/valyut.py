

import requests  #pip install requests
data = requests.get(f'https://www.cbr-xml-daily.ru/daily_json.js').json()

kurs = input('qaysi valyutaga almashtirasiz --> ')
kurs = kurs.upper()
uz_sum = float(input("necha so'm bor sizda -->"))

rubl = uz_sum * data['Valute']["UZS"]['Value'] / data['Valute']["UZS"]['Nominal']
print(rubl,"--> rubl")
usd  = rubl / data['Valute'][kurs]['Value'] * data['Valute'][kurs]['Nominal']
#rubl = data['Valute'][kurs]['Value'] * uz_sum /
print(usd )
#v['rates'][kurs] * y / v['rates']['UZS']

print(data)
print(type(data))
print(data.keys())
print(data['Date'])
print(data['Valute'])
print(data['Valute']['AUD'])
print(data['Valute']['AUD']['CharCode'],'-->',data['Valute']['AUD']['Value'],data['Valute']['AUD']["Name"])
print(data['Valute']['AUD']['CharCode'],'-->',data['Valute']['AUD']['Value'],data['Valute']['AUD']["Name"])


for i in data['Valute']:
	usd  = rubl / data['Valute'][i]['Value'] * data['Valute'][i]['Nominal']
	#rubl = data['Valute'][kurs]['Value'] * uz_sum /
	#print(usd )
	print(data['Valute'][i]['CharCode'], '-->', usd, data['Valute'][i]["Name"])

#print(data['Date'])
#print(data.keys())
#print(data['Valute'].keys())
#for i in data['Valute']:
#	print(i, '-->',data['Valute'][i]['Name'])


