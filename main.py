import requests
from bs4 import BeautifulSoup
import pandas as pd
url="https://codewithharry.com/"

req=requests.get(url)
htmlContent=req.content
#print(htmlContent)
soup=BeautifulSoup(htmlContent, 'html.parser')
#print(soup)
#print(soup.prettify())
title=soup.title
#print(title)
#print(title.string)
#print(type(soup))
#print(type(title))
#print(type(title.string))
para=soup.findAll('p')
#print(para)
anchors=soup.findAll('a')
#print(anchors)
#print(soup.find('p'))
#print(soup.find('p').get_text())
#print(soup.find('p')['class'])
classbasedpara=soup.find_all('p', class_="text-muted")
#print(soup.find_all('p', class_="text-muted"))
all_links=set()
for link in anchors:
    if link.get("href")!="#":
        link1="https://codewithharry.com"+link.get("href")
        all_links.add(link1)
        #print(link1)

all_links=list(all_links)
dat=soup.find(id="serverApp-state")
#print(dat)
df=pd.DataFrame({'anchs':all_links})
#print(df)
#df.to_csv('anchors.csv', index=False, encoding='utf-8')

elem = soup.select('.signupModal')
print(elem)

elem = soup.select('#loginModal')
print(elem)