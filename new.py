import requests


URL = "https://www.olx.ro/auto-masini-moto-ambarcatiuni/autoturisme/iasi_39939/?currency=EUR&search%5Bfilter_float_price:to%5D=5000"

response = requests.get(URL)
print(response.status_code)
