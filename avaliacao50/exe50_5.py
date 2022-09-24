"""
5) Criar um algoritmo que receba dois valores e pergunte ao usuario qual tipo de calculo deseja que
seja feito. (soma, subtração, multi´licação ou divisão) com a indicação do usuário, efetuar a operação
aritmética.
"""

num1 = input("Digite o primeiro valor: ")
num2 = input("Digite o segundo valor: ")

print("---------------------------")
print("1 - Soma                   ")
print("2 - Subtração              ")
print("3 - Multiplicação          ")
print("4 - Divisão                ")
print("---------------------------")
op = input("Escolha a operação: ")

if int(op) == 1:
    soma = int(num1) + int(num2)
    print("---------------------------------------------------")
    print(f"O resultado da soma dos números é: {soma}         ")
    print("---------------------------------------------------")

if int(op) == 2:
    sub = int(num1) - int(num2)
    print("---------------------------------------------------")
    print(f"O resultado da subtração dos números é: {sub}    ")
    print("---------------------------------------------------")

if int(op) == 3:
    mult = int(num1) * int(num2)
    print("---------------------------------------------------")
    print(f"O resultado da multiplicação dos números é: {mult}")
    print("---------------------------------------------------")

if int(op) == 4:
    divi = int(num1) / int(num2)
    print("---------------------------------------------------")
    print(f"O resultado da divisão dos números é: {divi}      ")
    print("---------------------------------------------------")


