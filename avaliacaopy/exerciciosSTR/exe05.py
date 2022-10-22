"""
5.	Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.
o	FULANO
o	FULAN
o	FULA
o	FUL
o	FU
o	F

"""

name = input("Escreva seu nome: ")
tamanho = len(name)
aux = 1

print("\n")
print("Seu nome em escadinha (invertida): ")
while aux <= tamanho:
    print(name[0:tamanho])
    tamanho = tamanho - 1
