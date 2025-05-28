def menu_lista():
    lista = []
    while True:
        print("\nMenu:")
        print("\n1 - Adicionar um elemento")
        print("\n2 - Remover o último elemento")
        print("\n3 - Mostrar elementos")
        print("\n4 - Sair")
        decision = input("Escolha uma opção: ")
        if decision == "1":
            elemento = input("Digite o elemento para adicionar: ")
            lista.append(elemento)
            print(f"'{elemento}' adicionado.")
        elif decision == "2":
            if lista:
                removido = lista.pop()
                print(f"'{removido}' removido.")
            else:
                print("A lista está vazia.")
        elif decision == "3":
            if lista:
                print("Elementos na lista:")
                for i, elem in enumerate(lista, 1):
                    print(f"{i}: {elem}")
            else:
                print("A lista Já está sem nada!")
        elif decision == "4":
            print("\nFechando >>>")
            break
        else:
            print("Opção inválida <<<")
menu_lista()