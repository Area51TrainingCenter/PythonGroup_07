import requests
from bs4 import BeautifulSoup

respuesta = requests.get('http://www.kitco.com/', headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'})

soup = BeautifulSoup(respuesta.content, 'html.parser')
venta = soup.find('span', attrs={'id': 'AU-bid'}).text
compra = soup.find('span', attrs={'id': 'AU-ask'}).text
bajo = soup.find('span', attrs={'id': 'AU-low'}).text
alto = soup.find('span', attrs={'id': 'AU-high'}).text

print('PRECIO DEL ORO:')
print('venta: {}'.format(venta))
print('compra: {}'.format(compra))
print('bajo: {}'.format(bajo))
print('alto: {}'.format(alto))
