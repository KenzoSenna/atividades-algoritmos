lista = [int((input(f"Digite o {num+1}° número: "))) for num in range(10)]
[lista.remove(x) for x in lista if x % 2 == 0]
print(lista)
