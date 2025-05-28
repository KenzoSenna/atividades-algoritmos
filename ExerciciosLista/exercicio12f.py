lista_num = [int(input(f"Digite o {x+1}° número: ")) for x in range(5)]
maior_que_10 = [num for num in lista_num if num > 10]
print(maior_que_10)