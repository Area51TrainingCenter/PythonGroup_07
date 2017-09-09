archivo = open('quijote.txt')
texto = archivo.read()
archivo.close()

# {'a': 1, 'b': 2, ....}
letras = {}

for letra in texto:
    if letra in 'abcdefghijklmnñopqrstuvwxyzáéíóúABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚ':
        if letra not in letras:
            letras[letra] = 1
        else:
            letras[letra] += 1

print(letras)
