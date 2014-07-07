import urllib2
import json
from dateutil.rrule import *
from dateutil.parser import *

# Variables
daySt = "20140601" # state date
dayEnd = "20140602" # end date
outPath = '/Users/dtodd/Documents/Work/Weather/' # output path
station = 'KDEW' # weather station ID
api = 'b316a72d2e91b2e7' # developer API key

# Create list of dates between start and end
days = list(rrule(DAILY, dtstart=parse(daySt), until=parse(dayEnd)))

# Create daily url, fetch json file, write to disk
for day in days:
	url = 'http://api.wunderground.com/api/' + api + '/history_' + day.strftime("%Y%m%d") + '/q/' + station + '.json'
	response = urllib2.urlopen(url)
	data = json.load(response)
	with open(outPath + station + '_' + day.strftime("%Y%m%d") + '.json', 'w') as outfile:
		json.dump(data, outfile)