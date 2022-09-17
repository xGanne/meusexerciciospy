"""
Exercício 01
Questão 5
Aluno: Felipe Augusto Claudino Ramos
Data: 29/08/2022
"""
# ENTRADA DE DADOS
salario = input("Digite seu salario: ")
reajuste = input("Digite o valor do reajuste (inteiro): ")
newR = float(salario) * int(reajuste) / 100
newSal = float(salario) + float(newR)

#FUNÇÕES
print(f"Antigo salário: {salario}")
print(f"Porcentagem do reajuste: {reajuste}%")
print(f"Valor do aumento: {newR}")
print(f"Novo salário: {newSal}")
