"""
6.	Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
Depois modifique o programa para que ele mostre os números um ao lado do outro.
"""

numero = 0

while numero <= 20:
    print(numero)
    numero = numero + 1

tabela = list(range(numero))
print(tabela)
