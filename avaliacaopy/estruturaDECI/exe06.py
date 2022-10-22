"""
6.	Faça um Programa que leia três números e mostre o maior deles.
"""

num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")
num3 = input("Digite o terceiro número: ")

if num1 > num2 and num1 > num3:
    print(f"O maior número é o primeiro: {num1}")
if num2 > num1 and num2 > num3:
    print(f"O maior número é o segundo: {num2}")
if num3 > num1 and num3 > num2:
    print(f"O maior número é o terceiro: {num3}")
if num1 == num2 and num1 == num3:
    print("Os números são iguais.")