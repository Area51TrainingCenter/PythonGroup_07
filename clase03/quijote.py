import re

archivo = open('quijote.txt')
texto = archivo.read()
archivo.close()

resultados = re.findall('\w+oso', texto.lower())
print('resultado: {}'.format(len(resultados)))
