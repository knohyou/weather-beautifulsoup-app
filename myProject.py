# Web scrapping National Weather service with BeautifulSoup 

# Simple site to download the page
import requests

page = requests.get('http://dataquestio.github.io/web-scraping-pages/simple.html')
#page Code 200 indicates successful request
#page.content # Show the downloaded html document

#
from bs4 import BeautifulSoup
# Let Beautifulsoup class parse document
soup = BeautifulSoup(page.content, 'html.parser') 
print(soup.prettify())

list(soup.children)
[type(item) for item in list(soup.children)]
# [bs4.element.Doctype, bs4.element.NavigableString, bs4.element.Tag]
# All items are beautiful soup objects
html = list(soup.children)[2]
list(html.children)
body = list(html.children)[3]
p = list(body.children)[1]
p.get_text()

# Find all instances of a tag at once instead
soup = BeautifulSoup(page.content,'html.parser')
soup.find_all('p') # Returns a list
soup.find_all('p')[0].get_text()
soup.find('p').get_text() # Returns first instance of a tag


## Searching for tags by class and id
import requests
page = requests.get('http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html')

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())
soup.find_all('p',class_='outer-text')
soup.find_all(class_='outer-text')
soup.find_all(id='first')

# Use CSS Selectorswith select method
soup.select("div p")


## Download Weather data
import requests
page = requests.get('https://forecast.weather.gov/MapClick.php?lat=35.9954&lon=-78.8964#.WrQKpYj49PY')
page.status_code

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())

seven_day = soup.find(id = 'seven-day-forecast-list')
forecast_items = seven_day.find_all(class_='tombstone-container')
tonight = forecast_items[0]
print(tonight.prettify())
short_description = tonight.find(class_='short-desc').get_text()
period = tonight.find(class_='period-name').get_text()
temperature = tonight.find(class_='temp').get_text()

print(period)
print(short_description)
print(temperature)

img = tonight.find('img')
desc = img['title']
print(desc)


## Extracting all information from the page
period_tags = seven_day.select('.tombstone-container .period-name')
periods = [period.get_text() for period in period_tags]
periods

temp_tags = seven_day.select('.tombstone-container .temp')
temp = [temperature.get_text() for temperature in temp_tags]
temp

short_desc = [short_desc.get_text() for short_desc in seven_day.select('.tombstone-container .short-desc')]
desc = [desc['title'] for desc in seven_day.select('.tombstone-container img')]

import pandas as pd
weather = pd.DataFrame({
            "period":periods,
            "short_desc":short_desc,
            "temperature":temp,
            "description":desc                        
                    })

temp_nums = weather["temperature"].str.extract("(?P<temp_num>\d+)",expand=False)
weather["temp_nums"] = temp_nums.astype('int')
temp_nums

weather["temp_nums"].mean()

# Only consider temperature at night
is_night = weather["temperature"].str.contains("Low")
weather["is_night"] = is_night

weather[is_night]


## Reference Tutorial
#https://www.dataquest.io/blog/web-scraping-tutorial-python/