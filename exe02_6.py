"""
Exercício 02
Questão 6
Aluno: Felipe Augusto Claudino Ramos
Data: 09/09/2022
"""
valor = 't'
resp = 'y'
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
        total = int(soma) * int(quantidade)
        media = int(total) / int(quantidade)
        num += 1
        resp = str(input("Deseja continuar?(s/n) "))

    if resp == 'n':
        print(f"O valor total em estoque é: {total}")
        print(f"A media de valor das mercadorias é: {media}")
