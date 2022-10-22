"""
13.	Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
-	Para homens: (72.7*h) - 58
-	Para mulheres: (62.1*h) - 44.7
"""

altura = input("Escreva sua altura (metros): ")
resp = input("Escreva seu sexo (mulher/homem): ")

if resp == 'mulher':
    calculo = (float(altura) * 62.1) - 44.7
    convert = round(calculo, 2)
    print(f"De acordo com a sua altura e seu sexo, seu peso ideal é: {convert}kg")

if resp == 'homem':
    calculo = (float(altura) * 72.7) - 58
    convert = round(calculo, 2)
    print(f"De acordo com a sua altura e seu sexo, seu peso ideal é: {convert}kg")