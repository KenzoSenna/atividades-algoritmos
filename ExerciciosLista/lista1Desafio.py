import random
lista_alunos = []; nota1 = 0; nota2 = 0; nota3 = 0; nota4 = 0; soma = 0
aprovados = 0; desaprovados = 0 # ou reprovados (como preferir chamar)
lista_media_aluno = []
cinco_piores = []
cinco_melhores = []
for contador in range(50):
    lista_alunos.append(1+contador)
for _ in lista_alunos:
    nota1 = random.randint(0, 100)
    nota2 = random.randint(0, 100)
    nota3 = random.randint(0, 100)
    nota4 = random.randint(0, 100)
    media_aluno = (nota1 + nota2 + nota3 + nota4) / 4
    lista_media_aluno.append(media_aluno)
for nota in lista_media_aluno:
    soma += nota
media_total = soma / 50
for nota in lista_media_aluno:
    if nota < media_total:
        desaprovados += 1
    else:
        aprovados += 1

menor_nota = min(lista_media_aluno)
maior_nota = max(lista_media_aluno)
posicao = lista_media_aluno.index(maior_nota)
for _ in range(5):
    cinco_piores.append(lista_media_aluno.pop(lista_media_aluno.index(min(lista_media_aluno))))
for _ in range(5):
    cinco_melhores.append(lista_media_aluno.pop(lista_media_aluno.index(max(lista_media_aluno))))
print(f"Lista alunos >>>\n{lista_alunos}\nSuas Notas >>>\n{lista_media_aluno}")
print(f"\nMédia para aprovação: {media_total}")
print(f"\nQuantidade de aprovados: {aprovados}\nQuantidade de reprovados: {desaprovados}")
print(f"\nMaior nota: {maior_nota} | Posição: {posicao + 1}")
print(f"\nPorcentagem de aprovados: {(aprovados / 50) * 100:.2f}%\nPorcentagem de desaprovados: {(desaprovados / 50) * 100:.2f}%")
print(f"\nCinco melhores notas: \n{cinco_melhores}\nCinco piores notas:\n{cinco_piores}")