v = {
    "disclaimer": "https://www.cbr-xml-daily.ru/#terms",
    "date": "2024-03-07",
    "timestamp": 1709758800,
    "base": "RUB",
    "rates": {
        "AUD": 0.01699284,
        "AZN": 0.01881754,
        "GBP": 0.0086939587,
        "AMD": 4.471272,
        "BYN": 0.035515399,
        "BGN": 0.01995514,
        "BRL": 0.0547756,
        "HUF": 4.006474,
        "VND": 265.847855,
        "HKD": 0.08644985,
        "GEL": 0.02942846969,
        "DKK": 0.07605488,
        "AED": 0.040651398,
        "USD": 0.0110691467,
        "EUR": 0.01018312,
        "EGP": 0.3419867,
        "INR": 0.91780168,
        "IDR": 174.4056256,
        "KZT": 4.98698397,
        "CAD": 0.0150341,
        "QAR": 0.0402917,
        "KGS": 0.98991278868,
        "CNY": 0.079960979,
        "MDL": 0.1964385687,
        "NZD": 0.0182238,
        "NOK": 0.1170783,
        "PLN": 0.04386696,
        "RON": 0.05060037,
        "XDR": 0.00833495,
        "SGD": 0.0148614467,
        "TJS": 0.121299,
        "THB": 0.396041,
        "TRY": 0.3494988,
        "TMT": 0.03874197,
        "UZS": 138.65644676,
        "UAH": 0.4249929876,
        "CZK": 0.2586967,
        "SEK": 0.1150925,
        "CHF": 0.009790656,
        "RSD": 1.19485,
        "ZAR": 0.209088,
        "KRW": 14.771768786,
        "JPY": 1.6602608
    }
}









y = float(input('necha rubl bor sizda -->'))
x = input('qaysi valyutaga almashtirasiz --> ')
x = x.upper()
#print(v['rates'].keys())
for i in v['rates'].keys():
    #print(i)
    if x == i:
        print(y,v['base'],' = ',v['rates'][i] * y,i)
        print(type(v['rates'][i]))
