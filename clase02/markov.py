from random import choice

archivo = open('quijote.txt')
texto = archivo.read()
archivo.close()

texto = texto.lower().replace('\n', ' ').replace('  ', ' ').replace('  ', ' ')
texto = ''.join(filter(lambda caracter: caracter in 'abcdefghijklmnñopqrstuvwxyzáéíóú ', texto))
texto = texto.split(' ')

palabras = {}

for posicion_actual, palabra in enumerate(texto[:-1]):
    siguiente_palabra = texto[posicion_actual + 1]

    if palabra not in palabras:
        palabras[palabra] = []

    palabras[palabra].append(siguiente_palabra)


cantidad_palabras = 10
oracion = [choice(list(palabras.keys()))]
# oracion = ['el']

for _ in range(cantidad_palabras):
    ultima_palabra = oracion[-1]
    nueva_palabra = choice(palabras[ultima_palabra])
    oracion.append(nueva_palabra)

print(' '.join(oracion))
