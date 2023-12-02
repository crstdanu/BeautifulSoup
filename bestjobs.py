from bs4 import BeautifulSoup
import requests


URL_best = "https://www.bestjobs.eu/ro/locuri-de-munca-in-iasi/python"

response = requests.get(URL_best).text


soup = BeautifulSoup(response, "lxml")

jobs = soup.find_all('div', class_="col mb-5 js-card-item card-item job-card")

for job in jobs:
    job_title = job.find('span', class_="d-none").text
    print(job_title)
