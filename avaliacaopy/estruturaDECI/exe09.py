"""
9.	Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""

num1 = input("Escreva o primeiro número: ")
num2 = input("Escreva o segundo número: ")
num3 = input("Escreva o terceiro número: ")

if num1 < num2 and num1 < num3 and num2 < num3:
    print(f"{num3}")
    print(f"{num2}")
    print(f"{num1}")

if num2 > num1 and num2 > num3 and num1 > num3:
    print(f"{num2}")
    print(f"{num1}")
    print(f"{num3}")
if num3 < num2 and num3 < num1 and num2 < num1:
    print(f"{num1}")
    print(f"{num2}")
    print(f"{num3}")
if num3 > num2 and num3 > num1 and num2 < num1:
    print(f"{num3}")
    print(f"{num1}")
    print(f"{num2}")
if num2 > num3 and num2 > num1 and num3 > num1:
    print(f"{num2}")
    print(f"{num3}")
    print(f"{num1}")
if num1 > num2 and num1 > num3 and num2 < num3:
    print(f"{num1}")
    print(f"{num3}")
    print(f"{num2}")