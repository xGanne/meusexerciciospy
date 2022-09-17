"""
Exercício 01
Questão 7
Aluno: Felipe Augusto Claudino Ramos
Data: 31/08/2022
"""
# ENTRADA DE DADOS
salario = input("Escreva seu salario: ")
totalV = input("Escreva o valor total de suas vendas: ")
carros = input("Escreva quantos carros vendeu: ")
comissao = input("Escreva a porcentagem recebida por carros vendidos (inteiro): ")
porcentV = float(totalV) * 5 /100
comissV = float(carros) * float(comissao) / 100
salarioF = float(salario) + float(porcentV) + float(comissV)

#FUNÇÕES
print(f"Seu salario: R${salario}")
print(f"Valor total de suas vendas: R${totalV}")
print(f"Quantos carros voce vendeu: {carros}")
print(f"Comissao por carros vendidos: {comissao}%")
print(f"Salario final: R${salarioF}")