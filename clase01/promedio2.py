notas = []

cantidad_notas = int(input('cantidad de notas: '))

for n in range(cantidad_notas):
    nota = float(input('nota No {}: '.format(n + 1)))
    notas.append(nota)

suma = 0
for nota in notas:
    suma += nota

promedio = suma / len(notas)
print('tu promedio es {}'.format(promedio))

if promedio < 11:
    print('jalaste :(')
else:
    print('aprobaste :)')
