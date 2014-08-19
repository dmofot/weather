import sys
import requests
import csv
from dateutil.rrule import *
from dateutil.parser import *

# Variables
daySt = sys.argv[1] # start date in yyyymmdd format, 20140710
dayEnd = sys.argv[2] # end date in yyyymmdd format, 20140712
outPath = '/Users/dtodd/Documents/Work/Weather/' # output path
station = 'KDEW' # weather station ID
api = 'b316a72d2e91b2e7' # developer API key

# Create list of dates between start and end
days = list(rrule(DAILY, dtstart=parse(daySt), until=parse(dayEnd)))

with open(outPath + station + '_' + daySt + '-' + dayEnd + '.csv', 'wb') as csvfile:
	f = csv.writer(csvfile)
	f.writerow(["datetime", "tempm", "tempi", "dewptm", "dewpti", "hum", "wspdm", "wspdi", "wgustm", "wgusti", "wdird", "wdire", "vism", "visi", "pressurem", "pressurei", "windchillm", "windchilli", "heatindexm", "heatindexi", "precipm", "precipi", "conds", "fog", "rain", "snow", "hail", "thunder", "tornado"])
	# Create daily url, fetch json file, write to disk
	for day in days:
		r = requests.get('http://api.wunderground.com/api/' + api + '/history_' + day.strftime("%Y%m%d") + '/q/' + station + '.json')
		data = r.json()['history']['observations']
		for elem in data:
			f.writerow([elem["utcdate"]["year"] + elem["utcdate"]["mon"] + elem["utcdate"]["mday"] + 'T' + elem["utcdate"]["hour"] + elem["utcdate"]["min"], elem["tempm"], elem["tempi"], elem["dewptm"], elem["dewpti"], elem["hum"], elem["wspdm"], elem["wspdi"], elem["wgustm"], elem["wgusti"], elem["wdird"], elem["wdire"], elem["vism"], elem["visi"], elem["pressurem"], elem["pressurei"], elem["windchillm"], elem["windchilli"], elem["heatindexm"], elem["heatindexi"], elem["precipm"], elem["precipi"], elem["conds"], elem["fog"], elem["rain"], elem["snow"], elem["hail"], elem["thunder"], elem["tornado"]])
