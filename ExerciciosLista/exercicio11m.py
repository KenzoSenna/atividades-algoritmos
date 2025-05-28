def verificadora_suprema(lista):
    lista_ordenada = sorted(lista)
    if lista == lista_ordenada:
        print("está ordenada")
    else:
        print("não está ordenada!")
lista = [1, 2, 3, 4, 6, 5]
verificadora_suprema(lista)