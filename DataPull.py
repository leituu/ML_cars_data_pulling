##
from bs4 import BeautifulSoup
import requests
##
page = requests.get("https://listado.mercadolibre.com.ar/clio#D[A:clio]")
soup = BeautifulSoup(page.content, 'html.parser')
##
body = soup.find('body')

##
main = body.find('main')
##
car_sect = soup.find('body').find('main').find('div').find('div').find('section').find
##
for car in car_sect:
    print(car)


##

