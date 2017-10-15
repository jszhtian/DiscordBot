import urllib.parse
import urllib.request
import asyncio
import re
import time
from bs4 import BeautifulSoup

contentstr='https://s.vndb.org/cv/63/17863.jpg'
query_string=urllib.parse.quote_plus(contentstr)
url="https://www.google.com/searchbyimage?&image_url="+query_string
user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'
req=urllib.request.Request(url,None,{'User-Agent':user_agent})
response=urllib.request.urlopen(req)
page=response.read()
soup=BeautifulSoup(page,'html.parser')
pos=soup.find('a',attrs={'class':'_gUb'})
print(pos.getText())
