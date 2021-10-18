import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

r=requests.get(url)
#print(r.content)

soup=BeautifulSoup(r.content, 'html.parser')
#print(soup.prettify())

#desc=soup.findAll('a', class_='_1fQZEK')
desc=soup.findAll('div', class_='_4rR01T')
#print(desc)

links=set()

for i in desc:
#    link=""
    links.add(i.string)



price=soup.findAll('div', class_='_30jeq3 _1_WHN1')

#print(price)

divclass=soup.findAll('div', class_='_2kHMtA')
#print(divclass)

dict1={}
prices=[]
descs=[]
for i in divclass:
    #if i.findAll('div', class_='_4rR01T'):
    dict1[i.find('div', class_='_4rR01T').string]=i.find('div', class_='_30jeq3 _1_WHN1').string
    descs.append(i.find('div', class_='_4rR01T').string)
    prices.append(i.find('div', class_='_30jeq3 _1_WHN1').string)

#print(dict1)

#df=(pd.DataFrame(dict1)).reset_index()
df=pd.DataFrame(dict1, index=[0])
print(df)
df1=pd.DataFrame({'Product':descs, 'Prices':prices})
print(df1)

df1.to_csv('LaptopPriceAll.csv', encoding='utf-8')

#df.to_csv('Laptop_Prices.csv', index=True, encoding='utf-8')
print('Hope CSV gets created.')