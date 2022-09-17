"""
Exercício 01
Questão 6
Aluno: Felipe Augusto Claudino Ramos
Data: 31/08/2022
"""
# ENTRADA DE DADOS
carro = input("Digite o valor do carro: ")
percent = float(carro) * 28 / 100
impostos = float(carro) * 45 / 100
total = float(carro) + float(percent) + float(impostos)

#FUNÇÕES
print(f"Valor do carro: R${carro}")
print(f"Valor do percentual do distribuidor: R${percent}")
print(f"Valor dos impostos: R${impostos}")
print(f"Total a gastar: R${total}")

