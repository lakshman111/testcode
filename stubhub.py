import json
import urllib.request
import pandas as pd

# http://stackoverflow.com/questions/22770917/scrapy-scraping-price-data-from-stubhub
# https://www.stubhub.com/boston-bruins-tickets-boston-bruins-boston-td-garden-3-3-2016/event/9341462/


webservice_url = "http://www.stubhub.com/ticketAPI/restSvc/event/9341462"
data = json.loads(urllib.request.urlopen(webservice_url).read().decode("utf8"))

tickets = data['eventTicketListing']['eventTicket']

#for i in range(len(tickets)):
#  section = tickets[i]['st']
#  row = tickets[i]['rd']
#  price = tickets[i]['cp']
#  quantity = tickets[i]['qt']

df = pd.DataFrame()
df['section'] = [x['st'] for x in tickets]
df['row'] = [x['rd'] for x in tickets]
df['price'] = [x['cp'] for x in tickets]
df['quantity'] = [x['qt'] for x in tickets]
print(df.head(20))