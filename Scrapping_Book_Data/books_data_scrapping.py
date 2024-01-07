from bs4 import BeautifulSoup
import requests
import pandas as pd
Names_of_books = []
Books_Price = []
Stocks_Availability = []
for i in range(1,10):
    url = 'https://books.toscrape.com/catalogue/page-'+str(i)+'.html'
    t = requests.get(url)
    soup = BeautifulSoup(t.text, 'lxml')
    box = soup.find('div',class_='col-sm-8 col-md-9')

    names = box.find_all('article',class_='product_pod')

    for name in names:
        book_name = name.h3.text
        Names_of_books.append(book_name)

    prices = box.find_all('p',class_='price_color')

    for price in prices:
        Books_Price.append(price.text)


    availabilites = box.find_all('p',class_='instock availability')

    for i in availabilites:
        Stocks_Availability.append(i.text.replace('\n,','').strip())



df = pd.DataFrame({'Book Name':Names_of_books,'Price':Books_Price,'Availability':Stocks_Availability})

df.to_csv('C:/Users/dinesh/Downloads/Documents/books_data.csv')
