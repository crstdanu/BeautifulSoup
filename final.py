import requests
from bs4 import BeautifulSoup


URL = "https://www.olx.ro/auto-masini-moto-ambarcatiuni/iasi_39939/?currency=EUR&search%5Bfilter_float_price:to%5D=5000"

response = requests.get(URL)

soup = BeautifulSoup(response.content, "html.parser")

rezultate = soup.find_all('div', class_='css-1sw7q4x')[1:-1]


for item in rezultate:
    if ("Azi" in item.find('p', class_='css-veheph').text) and item.get('id') and (not item.find('div', class_='css-1jh69qu')) and item.find('div', class_='css-efx9z5'):
        ad_id = item.get('id')
        ad_raw_link = item.find('a', class_="css-rc5s2u").get('href')
        ad_name = item.find('h6', class_='css-16v5mdi').text
        price_raw = item.find('p', class_='css-10b0gli').text
        ad_price = ''
        for el in price_raw:
            if el.isnumeric():
                ad_price += el
        anul_km = item.find('div', class_='css-efx9z5').text.strip()
        if "km" not in anul_km:
            anul = anul_km
            kilometraj = None
        elif ('km' in anul_km) and len(anul_km) < 11:
            anul = None
            kilometraj = anul_km.replace(' km', '')
        else:
            anul = anul_km[:4]
            kilometraj = ''
            for el in anul_km[4:]:
                if el.isnumeric():
                    kilometraj += el
