import os
import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def weather(): 
    
    ## Download Weather data
    page = requests.get('https://forecast.weather.gov/MapClick.php?lat=35.9954&lon=-78.8964#.WrQKpYj49PY')
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(page.content, 'html.parser')
    seven_day = soup.find(id = 'seven-day-forecast-list')
    
    ## Extracting all information from the page
    period_tags = seven_day.select('.tombstone-container .period-name')
    periods = [period.get_text() for period in period_tags]
    temp_tags = seven_day.select('.tombstone-container .temp')
    temp = [temperature.get_text() for temperature in temp_tags]
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

    mean_weather = weather["temp_nums"].mean()

    return render_template('index2.html', weather=weather)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

    
'''


# Only consider temperature at night
is_night = weather["temperature"].str.contains("Low")
weather["is_night"] = is_night

weather[is_night]


## Reference Tutorial
#https://www.dataquest.io/blog/web-scraping-tutorial-python/
'''