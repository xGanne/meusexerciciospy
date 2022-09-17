"""
Exercício 01
Questão 4
Aluno: Felipe Augusto Claudino Ramos
Data: 29/08/2022
"""
# ENTRADA DE DADOS
brancos = input("Digite a quantidade de votos brancos: ")
nulos = input("Digite a quantidade de votos nulos: ")
validos = input("Digite a quantidade de votos validos: ")
eleitores = int(brancos) + int(nulos) + int(validos)
porcentB = (float(brancos) / float(eleitores)) * 100
porcentN = (float(nulos) / float(eleitores)) * 100
porcentV = (float(validos) / float(eleitores)) * 100

#FUNÇÕES
print(f"Total de eleitores que votaram: {eleitores}")
print(f"Porcentagem de votos brancos: {porcentB}%")
print(f"Porcentagem de votos nulos: {porcentN}%")
print(f"Porcentagem de votos validos: {porcentV}%")