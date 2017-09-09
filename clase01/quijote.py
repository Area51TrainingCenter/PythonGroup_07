archivo = open('quijote.txt')
texto = archivo.read()
archivo.close()

caracteres = set()

for letra in texto:
    if letra not in 'abcdefghijklmnñopqrstuvwxyzáéíóúABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚ':
        caracteres.add(letra)

print('Simbolos: {}'.format(caracteres))
