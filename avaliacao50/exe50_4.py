"""
4) Criar um algoritmo que receba o salário de um funcionário e informe a ele o valor de desconto do INSS
e seu salário Líquido 7.5%
"""

salario = input("Informe seu salário: ")
salarioF = 0
inss = 0
aliq = 0

if float(salario) <= 1212:
    inss = (float(salario) * 7.5) / 100
    salarioF = float(salario) - float(inss)
    print("-----------------------------------------")
    print(f"Seu desconto do INSS é: R${inss}")
    print(f"Seu salário líquido é: R${salarioF}")
    print("-----------------------------------------")

if (float(salario) > 1212 and float(salario) <= 2427):
    aliq = 18.18
    inss = (float(salario) * 9 - float(aliq)) / 100
    salarioF = float(salario) - float(inss)
    print("-----------------------------------------")
    print(f"Seu desconto do INSS é: R${float(inss) - 18.18}")
    print(f"Seu salário líquido é: R${float(salarioF) - 18.18}")
    print("-----------------------------------------")

if (float(salario) > 2427 and float(salario) <= 3641):
    aliq - 91
    inss = (float(salario) * 12 - float(aliq)) / 100
    salarioF = float(salario) - float(inss)
    print("-----------------------------------------")
    print(f"Seu desconto do INSS é: R${float(inss) - 91}")
    print(f"Seu salário líquido é: R${float(salarioF) - 91}")
    print("-----------------------------------------")

if (float(salario) > 3641 and float(salario) <= 7087):
    inss = (float(salario) * 14) / 100
    salarioF = float(salario) - float(inss)
    print("-----------------------------------------")
    print(f"Seu desconto do INSS é: R${float(inss) - 163.82}")
    print(f"Seu salário líquido é: R${float(salarioF) - 163.82}")
    print("-----------------------------------------")
