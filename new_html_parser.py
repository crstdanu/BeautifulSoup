import requests
from bs4 import BeautifulSoup


URL = "https://www.olx.ro/auto-masini-moto-ambarcatiuni/autoturisme/iasi_39939/?currency=EUR&search%5Bfilter_float_price:to%5D=5000&search%5Bfilter_enum_petrol%5D%5B0%5D=petrol"

response = requests.get(URL).text
soup = BeautifulSoup(response, "html.parser")

titluri = soup.select(".css-rc5s2u")[0].get('href')

print(titluri)
# for titlu in titluri:
#     print(f"\n{titlu}")


# link_class = "css-rc5s2u"
