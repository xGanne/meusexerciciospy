"""
1.	Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
o	Compara duas strings
o	String 1: Brasil Hexa 2006
o	String 2: Brasil! Hexa 2006!
o	Tamanho de "Brasil Hexa 2006": 16 caracteres
o	Tamanho de "Brasil! Hexa 2006!": 18 caracteres
o	As duas strings são de tamanhos diferentes.
o	As duas strings possuem conteúdo diferente.
"""

frase1 = "Brasil Hexa 2006"
frase2 = "Brasil! Hexa 2006!"

print("\n")
print("Frase 1:")
print(frase1)
print("Frase 2:")
print(frase2)
print("\n")
print(f"O tamanho da primeira frase (caracteres): {len(frase1)}")
print(f"O tamanho da segunda frase (caracteres): {len(frase2)}")

if frase1 == frase2:
    print("\n")
    print("As frases são iguais")
else:
    print("\n")
    print("As frases são diferentes")

tamanhoS1 = len(frase1)
tamanhoS2 = len(frase2)

if tamanhoS1 == tamanhoS2:
    print("O tamanho das frases é o mesmo.")
else:
    print("O tamanho das frases é diferente.")
