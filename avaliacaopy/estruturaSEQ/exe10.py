"""
10.	Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
"""

temp = input("Escreva o valor da temperatura (Celsius): ")
fahren = (int(temp) * 1.8) + 32

print(f"A temperatura convertida para Fahrenheit é: {fahren}°F")