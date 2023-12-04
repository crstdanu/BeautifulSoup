import requests
from bs4 import BeautifulSoup
import json
from datetime import date
import time


URL = "https://www.olx.ro/auto-masini-moto-ambarcatiuni/iasi_39939/?currency=EUR&search%5Bfilter_float_price:to%5D=5000"


def scrape(URL):
    response = requests.get(URL).text
    soup = BeautifulSoup(response, "html.parser")
    titluri = soup.select(".css-1sw7q4x")

    # aici extrag toate ID-urile de pe pagina si le scriu intr-o lista
    car_id = []
    for titlu in titluri:
        if titlu.get('id'):
            car_id.append(titlu.get('id'))

    # aici caut anunturile in functie de ID
    # formez un dictionar pe care il scriu intr-un fisier .json

    for id in car_id:
        my_dict = {}
        car_ad = soup.find(id=f"{id}")
        ad_year_km = car_ad.find('div', class_="css-efx9z5")
        ad_location_date = car_ad.find("p", class_="css-veheph").text
        if ("Azi" in ad_location_date) and ad_year_km:
            ad_name = car_ad.find('h6', class_="css-16v5mdi").text
            ad_link = car_ad.find('a')['href']
            ad_price = car_ad.find('p', class_="css-10b0gli").text
            my_dict['ID'] = str(id)
            my_dict['nume anunt'] = str(ad_name)
            my_dict['link anunt'] = str(ad_link)
            my_dict['pret'] = str(ad_price)
            my_dict['anul si kilometrajul'] = str(ad_year_km.text)
            my_dict['data anuntului'] = str(date.today())
            my_dict['ora anuntului'] = str(ad_location_date[-4:])
            with open(f"masini/{id}.json", "w") as f:
                json.dump(my_dict, f, indent=4)


if __name__ == "__main__":
    while True:
        scrape(URL)
        print(time.localtime())
        time.sleep(600)
