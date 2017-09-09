nota1 = float(input('ingrese nota No 1: '))
nota2 = float(input('ingrese nota No 2: '))
nota3 = float(input('ingrese nota No 3: '))

promedio = (nota1 + nota2 + nota3) / 3
print('tu promedio es {}'.format(promedio))

if promedio < 11:
    print('jalaste :(')
else:
    print('aprobaste :)')
