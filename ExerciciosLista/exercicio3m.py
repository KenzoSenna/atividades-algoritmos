def apenas_oq_apareceu(lista):
    apareceu_ja = set()
    nao_tinha_aparecido = []
    for nome in lista:
        if nome not in apareceu_ja:
            nao_tinha_aparecido.append(nome)
            apareceu_ja.add(nome)
    return nao_tinha_aparecido
lista = ["kenzo", "kenzo", "pedro", "charles", "charles"]
print(apenas_oq_apareceu(lista))