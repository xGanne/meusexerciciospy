"""
11.	As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e
lhe contraram para desenvolver o programa que calculará os reajustes.

-	Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
baseado no salário atual:
-	salários até R$ 280,00 (incluindo) : aumento de 20%
-	salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
-	salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
-	salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
-	o salário antes do reajuste;
-	o percentual de aumento aplicado;
-	o valor do aumento;
-	o novo salário, após o aumento.

"""

salario = input("Escreva seu salário: R$")

if float(salario) <= 280.00:
    reajuste = (float(salario) * 20) / 100
    salarioF = float(salario) + float(reajuste)
    print("------------------------------------------------")
    print(f"Seu salário antes do reajuste: R${salario}")
    print("O percentual do reajuste é 20%")
    print(f"Seu aumento será de R${reajuste}")
    print(f"Seu salário após o aumento será R${salarioF}")
    print("------------------------------------------------")

if float(salario) > 280.00 and float(salario) <= 700.00:
    reajuste = (float(salario) * 15) / 100
    salarioF = float(salario) + float(reajuste)
    print("------------------------------------------------")
    print(f"Seu salário antes do reajuste: R${salario}")
    print("O percentual do reajuste é 15%")
    print(f"Seu aumento será de R${reajuste}")
    print(f"Seu salário após o aumento será R${salarioF}")
    print("------------------------------------------------")

if float(salario) > 700.00 and float(salario) < 1500.00:
    reajuste = (float(salario) * 10) / 100
    salarioF = float(salario) + float(reajuste)
    print("------------------------------------------------")
    print(f"Seu salário antes do reajuste: R${salario}")
    print("O percentual do reajuste é 10%")
    print(f"Seu aumento será de R${reajuste}")
    print(f"Seu salário após o aumento será R${salarioF}")
    print("------------------------------------------------")

if float(salario) >= 1500.00:
    reajuste = (float(salario) * 5) / 100
    salarioF = float(salario) + float(reajuste)
    print("------------------------------------------------")
    print(f"Seu salário antes do reajuste: R${salario}")
    print("O percentual do reajuste é 5%")
    print(f"Seu aumento será de R${reajuste}")
    print(f"Seu salário após o aumento será R${salarioF}")
    print("------------------------------------------------")

