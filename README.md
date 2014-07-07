weather
=======

Python scripts for parsing multiple days of historical weather data from Weather Underground

**NOTE:** _These scripts rely on the [Weather Underground](http://www.wunderground.com/) [API](http://www.wunderground.com/weather/api/).  You will need to obtain your own free API key [here](http://www.wunderground.com/weather/api/d/pricing.html)._

| Script | Description | Requirements |
| ------ | ----------- | ------------ |
| url2json_requests.py | Grabs JSON from URL and saves to JSON file | Reqeusts module |
| url2json_urllib.py | Grabs JSON from URL and saves to JSON file |  |
| url2json2csv_all.py | Grabs JSON from URL and saves to a single CSV file | Requests module |
| url2json2csv_daily.py | Grabs JSON from URL and saves to multiple daily CSV files | Requests module |

[Requests module](http://docs.python-requests.org/en/latest/) installation instructions found [here](http://docs.python-requests.org/en/latest/user/install/).

Variables to change:

| Variable | Description |
| -------- | ----------- |
| daySt | query start date in YYYYMMDD format |
| dayEnd | query end date  in YYYYMMDD format |
| outPath | path to output directory to save files (should already exist) |
| station | station ID (search [here](http://www.wunderground.com/history/)) |
| api | developer API Key obtained [here](http://www.wunderground.com/weather/api/d/pricing.html) |

Field descriptions [here](http://www.wunderground.com/weather/api/d/docs?d=resources/phrase-glossary).

Usage:
$ `python url2json2csv_all.py`
