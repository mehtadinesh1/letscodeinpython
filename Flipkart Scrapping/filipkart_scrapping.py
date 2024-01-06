import pandas as pd
from bs4 import BeautifulSoup
import requests
Product_name = []
Prices = []
Description = []
Reviews = []
url = "https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
r = requests.get(url,headers = headers)
soup = BeautifulSoup(r.text,'lxml')
box = soup.find("div",class_="_1YokD2 _3Mn1Gg")

names = box.find_all("div",class_="_4rR01T")
for name in names:
    Product_name.append(name.text)

prices  = box.find_all("div",class_="_30jeq3 _1_WHN1")

for price in prices:
        Prices.append(price.text)


descriptions = box.find_all('ul',class_='_1xgFaf')
for desc in descriptions:
        Description.append(desc.text)


reviews = box.find_all('div',class_='_3LWZlK')
for review in reviews:
        Reviews.append(review.text)

#print(len(Reviews),len(Product_name),len(Prices),len(Description))

df = pd.DataFrame({'Product_Name':Product_name,'Price':Prices,"Description":Description,"Rating":Reviews})
df.to_csv("C:/Users/dinesh/Downloads/Documents/first.csv")












'''np = soup.find("a", class_='_1LKTO3').get("href")
    cnp = "https://www.flipkart.com" + np
    print(cnp)
while True:
    np = soup.find('a',class_ ='_1LKTO3').get('href')
    cnp = "https://www.flipkart.com"+np
    url = cnp
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'lxml')'''