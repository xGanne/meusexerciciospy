"""
6.	Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e
imprima a data com o nome do mês por extenso.
o	Data de Nascimento: 29/10/1973
o	Você nasceu em  29 de Outubro de 1973.
"""

dia = int(input("Digite o dia que você nasceu: "))
mes = int(input("Digite o mês que você nasceu (número): "))
ano = int(input("Digite o ano que você nasceu: "))

if mes == 1 and dia <= 31 and dia >= 1:
    print(f"Data de Nascimento: {dia}/0{mes}/{ano}")
    print(f"Você nasceu em {dia} de Janeiro de {ano}.")

if mes == 2 and dia <= 29 and dia >= 1:
    print(f"Data de Nascimento: {dia}/0{mes}/{ano}")
    print(f"Você nasceu em {dia} de Fevereiro de {ano}.")

if mes == 3 and dia <= 31 and dia >= 1:
    print(f"Data de Nascimento: {dia}/0{mes}/{ano}")
    print(f"Você nasceu em {dia} de Março de {ano}.")

if mes == 4 and dia <= 30 and dia >= 1:
    print(f"Data de Nascimento: {dia}/0{mes}/{ano}")
    print(f"Você nasceu em {dia} de Abril de {ano}.")

if mes == 5 and dia <= 31 and dia >= 1:
    print(f"Data de Nascimento: {dia}/0{mes}/{ano}")
    print(f"Você nasceu em {dia} de Maio de {ano}.")

if mes == 6 and dia <= 30 and dia >= 1:
    print(f"Data de Nascimento: {dia}/0{mes}/{ano}")
    print(f"Você nasceu em {dia} de Junho de {ano}.")

if mes == 7 and dia <= 31 and dia >= 1:
    print(f"Data de Nascimento: {dia}/0{mes}/{ano}")
    print(f"Você nasceu em {dia} de Julho de {ano}.")

if mes == 8 and dia <= 31 and dia >= 1:
    print(f"Data de Nascimento: {dia}/0{mes}/{ano}")
    print(f"Você nasceu em {dia} de Agosto de {ano}.")

if mes == 9 and dia <= 30 and dia >= 1:
    print(f"Data de Nascimento: {dia}/0{mes}/{ano}")
    print(f"Você nasceu em {dia} de Setembro de {ano}.")

if mes == 10 and dia <= 31 and dia >= 1:
    print(f"Data de Nascimento: {dia}/{mes}/{ano}")
    print(f"Você nasceu em {dia} de Outubro de {ano}.")

if mes == 11 and dia <= 30 and dia >= 1:
    print(f"Data de Nascimento: {dia}/{mes}/{ano}")
    print(f"Você nasceu em {dia} de Novembro de {ano}.")

if mes == 12 and dia <= 31 and dia >= 1:
    print(f"Data de Nascimento: {dia}/{mes}/{ano}")
    print(f"Você nasceu em {dia} de Dezembro de {ano}.")


