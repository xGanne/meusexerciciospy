"""
9.	Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
"""

temp = input("Escreva o valor da temperatura (Fahrenheit): ")
celsius = (int(temp) - 32) / 1.8

print(f"A temperatura convertida para Celsius é: {celsius}°C")