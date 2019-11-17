from requests_html import HTMLSession
import csv
URL = ’https://www.ip-adress.com/ip-address/ipv4/'
FILENAME = ‘ip.csv’
OUTNAME = ‘out.csv’
iplist = []
with open(FILENAME) as f:
   reader = csv.reader(f)
   iplist = [row for row in reader]
session = HTMLSession()
header = [‘IP Address’,‘Decimal Representation’,‘ASN’,‘City’,‘Country’,‘Country Code’,‘ISP’,‘Latitude’,‘Longitude’,‘Organization’,‘Postal Code’,‘Is Private IP Address’,‘PTR Resource Record’,‘Is Reserved IP Address’,‘State’,‘State Code’,‘Timezone’,‘Local Time’]
with open(OUTNAME,‘w’) as w:
   writer = csv.writer(w)
   writer.writerow(header)
   for ip in iplist:
       tmplist = []
       r = session.get(URL + ip[0])
       tds = r.html.find(‘td’)
       for td in tds:
           tmplist.append(td.text)
       writer.writerow(tmplist)
