def quicksort(numeros):
    if len(numeros) <= 1:
        return numeros
    primer_elemento = numeros[0]
    menores = [n for n in numeros if n < primer_elemento]
    mayores = [n for n in numeros if n > primer_elemento]

    return quicksort(menores) + [primer_elemento] + quicksort(mayores)

print(quicksort([5, 6, 9, 8, 2, 1, 7]))
