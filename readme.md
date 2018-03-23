# Demonstration of a simple web scrapping from [National weather service](https://www.weather.gov/) using [Beautifulsoup](https://pypi.python.org/pypi/beautifulsoup4).
Implement Flask web framework, bootstrap template, and deployed on Heroku 

Final product can be seen at https://weather-beautifulsoup-app.herokuapp.com/.

Follow instructions below to get the project running on your local machine and heroku. 

### Prerequisites
* Setup a free Heroku account
* Login heroku account ``` heroku login ``` 
* Python 
 
## Run initial test 
Copy the project into local machine using ```git clone```
https://github.com/knohyou/weather-beautifulsoup-app.git```
$ python app.py
```
Test code on local machine by visiting http://localhost:5000

## First time Deploying on Heroku
```
$ heroku create 
$ git init
$ git add .
$ git commit -m "Commit" 
$ git push heroku master
$ heroku ps:scale web=1
$ heroku open
```
If everything went smoothly, the final deployed application should be the same as mine. https://simple-heroku-flask.herokuapp.com/

## Running the app locally through heroku
If using Windows, run code below 
```
$ heroku local web -f Procfile.windows 
```
Open http://localhost:5000 in browser to see app running locally

## Note
```
Need to change 
<link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
to the following for the CSS files to be read by Flask
<link href="{{ url_for('static', filename='bootstrap.min.css') }}" rel="stylesheet">
``` 

## Acknowledgments
[National weather service](https://www.weather.gov/)
* https://github.com/bev-a-tron/MyFlaskTutorial
* Bokeh code pulled from https://github.com/bokeh/bokeh/tree/master/examples/embed/simple


