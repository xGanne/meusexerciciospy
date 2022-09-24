"""
Exercício 02
Questão 6
Aluno: Felipe Augusto Claudino Ramos
Data: 09/09/2022
"""
valor = 't'
resp = 's'
quantidade = 0
total = 0
media = 0
aux = 0
aux2 = 0
num = 1
soma = 0

while resp == 's':
        aux += 1
        valor = input(f"Digite o valor da mercadoria {num}: R$")
        soma = soma + int(valor)
        quantidade += 1
        media = int(soma) / int(quantidade)
        num += 1
        resp = str(input("Deseja continuar?(s/n) "))

if resp == 'n':
        print("----------------------------------------------")
        print(f"O valor total em estoque é: {soma}")
        print(f"A media de valor das mercadorias é: {media}")
        print("----------------------------------------------")
