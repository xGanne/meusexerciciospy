"""
Exercício 01
Questão 3
Aluno: Felipe Augusto Claudino Ramos
Data: 29/08/2022
"""
# ENTRADA DE DADOS
anos = input("Digite quantos anos voce tem atualmente: ")
meses = input("Digite quantos meses passaram apos seu aniversario (atualmente): ")
dias = input("Digite quantos dias passaram apos seu aniversario (atualmente): ")
totalM = (365 * int(anos)) + (30 * int(meses)) + int(dias)

#FUNÇÕES
print(f"Anos escritos anteriormente: {anos}")
print(f"Meses escritos anteriormente: {meses}")
print(f"Dias escritos anteriormente: {dias}")
print(f"Sua idade em dias: {totalM}")