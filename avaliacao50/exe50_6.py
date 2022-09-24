"""
6) Criar um programa que calcule celsius para fahrenheit e a contrario.
"""

num = input("Escreva o valor: ")

print("---------------------------")
print("1 - Celsius para Farenheit ")
print("2 - Fahrenheit para Celsius")
print("---------------------------")
op = input("Escolha a opção: ")

if int(op) == 1:
    fahren = int(num) * 1.8 + 32
    print(f"{num} em Fahrenheit é: {fahren}")

if int(op) == 2:
    celsius = (int(num) - 32) / 1.8
    print(f"{num} em Celius é: {celsius}")
