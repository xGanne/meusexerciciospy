"""
3.	Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.
o	F
o	U
o	L
o	A
o	N
o	O

"""

aux = ""
name = input("Digite seu nome: \n")

for caractere in name:
    aux = aux + caractere + "\n"

print("Seu nome em vertical:")
print(aux)

