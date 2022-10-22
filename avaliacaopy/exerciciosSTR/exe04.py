"""
4.	Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.
o	F
o	FU
o	FUL
o	FULA
o	FULAN
o	FULANO

"""

name = input("Escreva seu nome: ")
tamanho = len(name)
aux = 1

print("\n")
print("Seu nome em escadinha: ")
while aux <= tamanho:
    print(name[0:aux])
    aux = aux + 1
