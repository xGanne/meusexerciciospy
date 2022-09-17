"""
Exercício 02
Questão 1
Aluno: Felipe Augusto Claudino Ramos
Data: 09/09/2022
"""
nota1 = input("Digite a primeira nota: ")
nota2 = input("Digite a segunda nota: ")
nota3 = input("Digite a  terceira nota: ")
result = (float(nota1) + float(nota2) + float(nota3)) / 3

if result >= 9.0:
    print(f"Sua avaliação foi A, e sua media foi: {result}")

if ((result >= 7.5) and (result < 9.0)):
    print(f"Sua avaliação foi B, e sua media foi: {result}")

if ((result >= 6.0) and (result < 7.5)):
    print(f"Sua avaliação foi C, e sua media foi: {result}")

if result < 6.0:
    print(f"Sua avaliação foi D, e sua media foi: {result}")