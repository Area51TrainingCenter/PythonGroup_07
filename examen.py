import re

with open('clase01/quijote.txt') as archivo:
    contenido = archivo.read()

contenido = contenido.lower()
contenido = ''.join(filter(lambda x: x in '\n abcdefghijklmnñopqrstuvwxyzáéíóúABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚ', contenido))
contenido.replace('\n', ' ').replace('  ', ' ').replace('  ', ' ')
contenido = contenido.split(' ')

palabras = {
    'el': {},
    'la': {},
    'los': {},
    'las': {}
}

for posicion, posible_palabra in enumerate(contenido[:-1]):
    if posible_palabra in ('el', 'la', 'los', 'las'):
        articulo = posible_palabra
        palabra = contenido[posicion + 1]
        if palabra not in palabras[articulo]:
            palabras[articulo][palabra] = 0
        palabras[articulo][palabra] += 1


for articulo, ranking in palabras.items():
    print(articulo)
    ranking = sorted(ranking.items(), key=lambda i: i[1], reverse=True)
    for palabra, veces in ranking[:10]:
        print('  {}: {}'.format(palabra, veces))

    print('=================')
