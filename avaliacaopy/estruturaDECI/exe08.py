"""
8.	Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
sabendo que a decisão é sempre pelo mais barato.
"""

produto1 = input("Informe o preço do primeiro produto: ")
produto2 = input("Informe o preço do segundo produto: ")
produto3 = input("Informe o preço do terceiro produto: ")

if produto1 < produto2 and produto1 < produto3:
    print(f"O produto que você deve comprar é o primeiro de R${produto1}")
if produto2 < produto1 and produto2 < produto3:
    print(f"O produto que você deve comprar é o segundo de R${produto2}")
if produto3 < produto2 and produto3 < produto1:
    print(f"O produto que você deve comprar é o terceiro de R${produto3}")