from functools import reduce
import string

nombres = [
    {'nombre': 'moisés', 'apellido': 'cachay'},
    {'nombre': 'josé', 'apellido': 'ruiz'},
    {'nombre': 'ana', 'apellido': '1'}
]


def filtro(resultado_anterior, elemento):
    validos = resultado_anterior[0]
    invalidos = resultado_anterior[1]

    caracteres_filtrados = filter(lambda letra: letra not in string.ascii_letters, elemento['apellido'])

    if list(caracteres_filtrados):
        invalidos += [elemento]
    else:
        validos += [elemento]

    return validos, invalidos
#                                   (validos, invalidos)
resultado = reduce(filtro, nombres, (     [],        []) )
print('validos: {}'.format(resultado[0]))
print('invalidos: {}'.format(resultado[1]))
