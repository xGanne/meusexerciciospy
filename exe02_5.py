"""
Exercício 02
Questão 5
Aluno: Felipe Augusto Claudino Ramos
Data: 09/09/2022
"""
quantidade = input("Digite quantos tipos de mercadoria há no estoque: ")
valor = 't'
total = 0
media = 0
aux = 0
aux2 = 0
num = 1
soma = 0

while int(aux) < int(quantidade):
    if int(quantidade) > 0:
        aux += 1
        valor = input(f"Digite o valor da mercadoria {num}: R$")
        soma = soma + int(valor)
        total = int(soma) * int(quantidade)
        media = int(total) / int(quantidade)
        num += 1

    if aux == int(quantidade):
        print(f"O valor total em estoque é: {total}")
        print(f"A media de valor das mercadorias é: {media}")
