""" 8.	Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês."""

valor = input("Escreva quando você ganha por hora: ")
horas = input("Escreva quantas horas você trabalhou no mês: ")

total = int(valor) * int(horas)

print(f"Seu salário mensal é: R${total}")