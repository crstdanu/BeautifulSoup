from bs4 import BeautifulSoup
import requests
import datetime
import json


URL = "https://www.olx.ro/auto-masini-moto-ambarcatiuni/autoturisme/iasi_39939/?currency=EUR&search%5Bfilter_float_price:to%5D=6000"


def scrape_cars(link):
    response = requests.get(link).text
    soup = BeautifulSoup(response, "lxml")
    cars = soup.find_all('a', class_="css-rc5s2u")

    for car in cars:
        car_add_data = car.find('p', class_="css-veheph er34gjf0").text
        if "Azi" in car_add_data:
            car_name = car.find('h6', class_="css-16v5mdi er34gjf0").text
            car_price = car.find(
                'p', class_="css-10b0gli er34gjf0").text.replace(" ", "")
            car_price_number = int(car_price.split("€")[0])
            car_an_km = car.find('div', class_="css-efx9z5").text
            if len(car_an_km) > 11:
                car_an = car_an_km[:4].strip()
                car_km = car_an_km[-10:].strip().replace(" km", "")
            else:
                car_an = None
                car_km = None
            car = {"Nume anunt": car_name, "Pret": car_price_number,
                   "Anul fabricatiei": car_an, "Kilometraj": car_km}


lista_masini = scrape_cars(URL)

print(lista_masini[0])


output = "lista_masini.json"
with open("output.json", "a") as f:
    json.dump(lista_masini, f, indent=4)
