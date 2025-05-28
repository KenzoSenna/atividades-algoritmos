lista = [1, 2, 3, 4, 5, 6]
lista_pares = [x for x in lista if x % 2 == 0]
lista_impares = [x for x in lista if not x % 2 == 0]
print(lista_pares)
print(lista_impares)