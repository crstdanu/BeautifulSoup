import requests


url = "https://www.olx.ro/auto-masini-moto-ambarcatiuni/autoturisme/iasi_39939/?currency=EUR"


response = requests.get(url)
with open("pagina.html", "wb") as f:
    f.write(response.content)
