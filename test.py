import urllib.parse
import urllib.request
import asyncio
import time
from bs4 import BeautifulSoup

class GetInfo():
    url=''
    soup=None
    def GetPage(self,url):
        self.url=url
        print('input URL:'+url)
        response=urllib.request.urlopen(url)
        html=response.read()
        return html
    def ExtractInfo(self,buf):
        if not self.soup:
            try:
                self.soup=BeautifulSoup(buf,'html.parser')
            except:
                print('Soup failed to get information:'+self.url)
                return
        title=self.soup.title.string
        Gamelist=[]
        if title.startswith("Bangumi"):
            uls=self.soup.find('ul',attrs={'id':'browserItemList'})
            lis = uls.find_all('li')
            for li in lis:
                try:
                    Gamelist.append(li.div.h3.a.getText())
                    Gamelist.append(li['id'])
                except:
                    pass
            return Gamelist
        else:
            infolist=['Game']
            imgURL=''
            divs=self.soup.find('div',attrs={'id':'bangumiInfo'})
            img=divs.find('div',attrs={'align':'center'})
            imgsrc=img.find('img')
            if(imgsrc):
                imgURL=imgsrc['src']
            infolist.append(imgURL)
            descdiv=self.soup.find('div',attrs={'id':'subject_detail'})
            desc=descdiv.find('div',attrs={'id':'subject_summary'})
            infolist.append(desc.getText())
            table = divs.find('ul', attrs={'id':'infobox'})
            rows = table.find_all('li')
            for row in rows:
                infolist.append(row.getText())
            return infolist

info=GetInfo()
buf=info.GetPage('http://bangumi.tv/subject/40297')
list=info.ExtractInfo(buf)
print(list)