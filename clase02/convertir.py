numero = input('grados sexagesimales: ')
try:
    numero = float(numero)
    resultado = (numero * 2 * 3.14) / 360
    print('radianes: {}'.format(resultado))
except (ValueError, KeyError) as e:
    print('fallo al interpretar el numero')
