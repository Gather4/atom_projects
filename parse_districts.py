#Some quick code to get the list of districts from an html file and output a list
#This will preserve the links for each school
#From url https://www.westchestergov.com/public-school-districts
#Parse all links as key value pairs
import urllib3
from bs4 import BeautifulSoup
http = urllib3.PoolManager()
raw = http.request('GET', 'https://www.westchestergov.com/public-school-districts')
if raw.status == 200:
    soup = BeautifulSoup( raw.data, 'html.parser')
    # Get the body of the website, which is where all of the links we want are
    main = soup.find('div', itemprop='articleBody')
    # Print out all the school district names and url's
    for link  in  main.find_all('a'):
        print( "%s, %s" %(link.text, link.get('href') ) )
