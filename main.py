from bs4 import BeautifulSoup
import requests


url = "https://www.olx.ro/auto-masini-moto-ambarcatiuni/autoturisme/iasi_39939/?currency=EUR&search%5Bfilter_float_price:to%5D=6000"

url_m = "https://m.olx.ro/auto-masini-moto-ambarcatiuni/autoturisme/iasi_39939/?currency=EUR"


response = requests.get(url).text

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
        car_an = car_an_km[:5]
        car_km = car_an_km[5:].strip()
        print()
        print(f"Masina: {car_name}")
        print(f"Pret: {car_price_number}€")
        print(f"An fabricatie: {car_an}")
        print(f"Kilometraj: {car_km}")
        print(f"Data anuntului: {car_add_data}")
