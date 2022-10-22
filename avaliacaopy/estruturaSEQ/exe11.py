"""
11.	Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
-	o produto do dobro do primeiro com metade do segundo .
-   a soma do triplo do primeiro com o terceiro.
-	o terceiro elevado ao cubo.
"""

num1 = input("Digite o primeiro numero (inteiro): ")
num2 = input("Digite o segundo numero (inteiro): ")
num3 = input("Digite o terceiro numero (real): ")

somaDobro = (int(num1) * 2) + (int(num2)/2)
somaTriplo = (int(num1) * 3) + float(num3)
elevado = float(num3) ** 3

print(f"O produto do dobro do primeiro número com metade do segundo número é: {somaDobro}")
print(f"A soma do triplo do primeiro número com o terceiro número é: {somaTriplo}")
print(f"O terceiro número elevado ao cubo é: {elevado}")
