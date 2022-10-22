"""
12.	Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
usando a seguinte fórmula: (72.7*altura) - 58,
"""

altura = input("Escreva sua altura (metros): ")
formula = (float(altura) * 72.7) - 58
convert = round(formula, 2)

print(f"De acordo com a sua altura, seu peso ideal é: {convert}kg")