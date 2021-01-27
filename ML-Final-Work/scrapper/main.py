import requests
from bs4 import BeautifulSoup

html_text = requests.get("https://stackoverflow.com/jobs")

soup = BeautifulSoup(html_text.content, 'lxml')

jobs = soup.find_all('div', class_='grid')
for job in jobs:
    job_link = job.find('div', class_='grid--cell f11')
    print(job_link)