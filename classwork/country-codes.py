from bs4 import BeautifulSoup
import requests

def getHTML(url):
    response = requests.get(url)
    return response.text

import requests
response = requests.get("https://www.countrycode.org")
print(response)

print(response.status_code)

html = getHTML("https://www.countrycode.org/")

soup = BeautifulSoup(html, 'html.parser')

table = soup.find('table', attrs = {'class':'main-table'})
tbody = table.find('tbody')

countries = []

for row in tbody.find_all('tr'):
    cells = row.find_all('td')
    country = {}
    country['name'] = cells[0].string    
    countrycodes = cells[2].string
    country['iso-2'] = countrycodes.split('/')[0]
    country['iso-3'] = countrycodes.split('/')[1]
    countries.append(country)

list(countries)