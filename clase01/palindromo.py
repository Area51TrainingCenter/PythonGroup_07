palabra = input('escribe una palabra: ')
palabra_al_reves = palabra[::-1]

if palabra == palabra_al_reves:
    print('es palindromo')
else:
    print('no es palindromo')
