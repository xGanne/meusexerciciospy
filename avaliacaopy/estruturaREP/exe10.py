"""
10.	Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo
compreendido por eles.
"""

num1 = int(input("Escreva o primeiro número: "))
num2 = int(input("Escreva o segundo número: "))

while num1 < (num2 - 1):
    num1 = num1 + 1
    print(num1)
