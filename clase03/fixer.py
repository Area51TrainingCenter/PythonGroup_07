import requests

respuesta = requests.get('http://api.fixer.io/latest')
respuesta = respuesta.json()

monto = float(input('Introduzca monto en euros: '))
tipo_cambio = respuesta['rates']['USD']
monto_convertido = monto * tipo_cambio

print('Resultado: {}'.format(monto_convertido))
