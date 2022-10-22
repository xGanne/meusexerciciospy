"""
10.	Faça um Programa que pergunte em que turno você estuda.
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""

resp = input("Em qual turno você estuda?\n"
             "M - Matutino\n"
             "v - Vespertino\n"
             "N - Noturno"
             ": ")

if resp == 'M':
    print("Bom Dia!")
if resp == 'V':
    print("Boa Tarde!")
if resp == 'N':
    print("Boa Noite!")
if resp != 'M' and resp != 'V' and resp != 'N':
    print("Valor Inválido!")