"""
Exercício 02
Questão 2
Aluno: Felipe Augusto Claudino Ramos
Data: 09/09/2022
"""
codigo = input("Informe seu codigo de empregado: ")
anoNas = input("Informe o ano de seu nascimento: ")
anoIng = input("Informe o ano de ingresso na empresa: ")
idade = 2022 - int(anoNas)
tempoTrab = 2022 - int(anoIng)

if idade >= 65:
    print(f"Sua idade: {idade}")
    print(f"Seu tempo de trabalho: {tempoTrab}")
    print("Requerer aposentadoria.")

if tempoTrab >= 30:
    print(f"Sua idade: {idade}")
    print(f"Seu tempo de trabalho: {tempoTrab}")
    print("Requerer aposentadoria.")

if ((tempoTrab >= 30) and (idade >= 60)):
    print(f"Sua idade: {idade}")
    print(f"Seu tempo de trabalho: {tempoTrab}")
    print("Requerer aposentadoria.")

if ((tempoTrab < 30) and (idade < 60)):
    print(f"Sua idade: {idade}")
    print(f"Seu tempo de trabalho: {tempoTrab}")
    print("Não requerer aposentadoria.")