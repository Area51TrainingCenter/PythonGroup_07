import requests
import pytesseract
from PIL import Image
from bs4 import BeautifulSoup

sesion = requests.Session()
sesion.get('http://www.sunat.gob.pe/cl-ti-itmrconsruc/jcrS00Alias')

respuesta_imagen = sesion.get('http://www.sunat.gob.pe/cl-ti-itmrconsruc/captcha?accion=image&nmagic=1')

with open('imagen.png', 'wb') as imagen:
    imagen.write(respuesta_imagen.content)

captcha = pytesseract.image_to_string(Image.open('imagen.png'))
print('CAPTCHA: {}'.format(captcha))

ruc = input('ingrese RUC: ')

informacion = {
    'accion': 'consPorRuc',
    'razSoc': '',
    'nroRuc': ruc,
    'nrodoc': '',
    'contexto': 'ti-it',
    'tQuery': 'on',
    'search1': ruc,
    'codigo': captcha,
    'tipdoc': '1',
    'search2': '',
    'coddpto': '',
    'codprov': '',
    'coddist': '',
    'search3': '',
}

respuesta = sesion.post('http://www.sunat.gob.pe/cl-ti-itmrconsruc/jcrS00Alias', data=informacion)

soup = BeautifulSoup(respuesta.content, 'html.parser')
primera_tabla = soup.find_all('table')[0]
filas = primera_tabla.find_all('tr')
textos = [fila.text.strip().replace('  ', '') for fila in filas]
resultado = '\n'.join(textos)
print(resultado)

