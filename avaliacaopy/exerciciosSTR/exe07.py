"""
7.	Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco),
conte:
o	quantos espaços em branco existem na frase.
o	quantas vezes aparecem as vogais a, e, i, o,

"""

contNULL = 0
contA = 0
contE = 0
contI = 0
contO = 0
contU = 0
frase = input("Escreva uma frase: ")

for caractere in frase:
    if caractere == ' ':
        contNULL = contNULL + 1
    if caractere.upper() == 'A':
        contA = contA + 1
    if caractere.upper() == 'E':
        contE = contE + 1
    if caractere.upper() == 'I':
        contI = contI + 1
    if caractere.upper() == 'O':
        contO = contO + 1
    if caractere.upper() == 'U':
        contU = contU + 1

print(f"Frase escrita:\n {frase}")
print(f"Quantidade de espaços na frase: {contNULL}")
print(f"Quantidade de letras A na frase: {contA}")
print(f"Quantidade de letras E na frase: {contE}")
print(f"Quantidade de letras I na frase: {contI}")
print(f"Quantidade de letras O na frase: {contO}")
print(f"Quantidade de letras U na frase: {contU}")


