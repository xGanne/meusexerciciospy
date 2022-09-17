"""
Exercício 02
Questão 3
Aluno: Felipe Augusto Claudino Ramos
Data: 09/09/2022
"""
num1 = input("Digite o primeiro numero: ")
num2 = input("Digite o segundo numero: ")

if int(num2) == 0:
    print("O segundo numero nao pode ser 0")
    num2 = input("Digite o segundo numero novamente: ")
    print(f"O resultado e: {int(num1) / int(num2)}")

else:
    print(f"O resultado e: {int(num1) / int(num2)}")