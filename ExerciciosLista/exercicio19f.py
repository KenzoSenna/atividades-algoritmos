lista_nomes = []
decision = ""
while decision != "sair":
    nome = str(input("Digite o nome que deseja adicionar a lista\nDigite (sair) - para sair\n: "))
    decision = nome
    if nome != "sair":
        lista_nomes.append(nome)
print(lista_nomes)