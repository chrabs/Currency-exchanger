from locale import currency
from tempfile import TemporaryFile
import requests
import json
from pprint import pprint

body = requests.get('http://api.nbp.pl/api/exchangerates/tables/A/')

currency = input('Jaka walute chcesz wymienić? [kod waluty]: ')
how_much = int(input('Ile waluty chcesz wymienić? : '))

try: 
    exchanger = body.json()
except json.JSONDecodeError:
    print("Niepoprawny format")
else:
    for rate in exchanger[0]['rates']:
        if currency == rate['code']:
            result = how_much * rate['mid']
            print(f'W rezultacie otrzymasz : {result} PLN')