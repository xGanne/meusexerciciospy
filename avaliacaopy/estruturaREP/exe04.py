"""
4.	Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3%
e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
Faça um programa que calcule e escreva o número de anos necessários para que a população do país
A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
"""

paisA = 80000
paisB = 200000
taxaA = int(paisA) * 0.03
taxaB = int(paisB) * 0.015
ano = 0
while int(paisA) <= int(paisB):
    print(f"Ano: {ano}")
    print(f"População do País A: {paisA}")
    print(f"População do País B: {paisB}")
    ano = ano + 1
    paisA = int(paisA) + int(taxaA)
    paisB = int(paisB) + int(taxaB)
    if paisA > paisB:
        print(f"\nNúmero de anos necessários para a população do país A ultrapasse a do país B: {ano}")