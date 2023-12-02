from bs4 import BeautifulSoup
import requests
import datetime
import json


URL = "https://www.olx.ro/auto-masini-moto-ambarcatiuni/autoturisme/iasi_39939/?currency=EUR&search%5Bfilter_float_price:to%5D=6000"


response = requests.get(URL).text
soup = BeautifulSoup(response, "lxml")
cars = soup.find_all('a', class_="css-rc5s2u")
car_list = []


for car in cars:
    query_link = car['href']
    print(f'https://www.olx.ro{query_link}')
    car_name = car.find('h6', class_="css-16v5mdi er34gjf0").text
    car_price = car.find(
        'p', class_="css-10b0gli er34gjf0").text.replace(" ", "")
    car_price_number = int(car_price.split("€")[0])
    print(car.a['href'])
    car_an_km = car.find('div', class_="css-efx9z5").text
    car_an = car_an_km[:4].strip()
    car_km = car_an_km[-10:].strip().replace(" km", "")
    car_list.append({
        "Nume anunt": car_name,
        "Pret": car_price_number,
        "Anul fabricatiei": car_an,
        "Kilometraj": car_km,
        "Detalii": None,
        "Data anuntului": None,
        "Ora anuntului": None
    })

# print(car_list)


# output = "lista_masini.json"
# with open("output.json", "a") as f:
#     json.dump(lista_masini, f, indent=4)