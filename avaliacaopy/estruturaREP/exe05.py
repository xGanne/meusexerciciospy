"""
5.	Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
Valide a entrada e permita repetir a operação.
"""
resp = "s"

while resp == "s":
    paisA = int(input("Escreva a população do país A: "))
    taxaA = int(input("Escreva a taxa de crescimento do país A: "))
    paisB = int(input("Escreva a população do país B: "))
    taxaB = int(input("Escreva a taxa de crescimento do país B: "))
    ano = 0
    calcA = 0
    calcB = 0

    while paisA <= paisB:
        print(f"Ano: {ano}")
        print(f"População do País A: {paisA}")
        print(f"População do País B: {paisB}")
        ano = ano + 1
        calcA = paisA * taxaA / 100
        calcB = paisB * taxaB / 100
        paisA = paisA + calcA
        paisB = paisB + calcB
        if paisA > paisB:
            print(f"\nNúmero de anos necessários para a população do país A ultrapasse a do país B: {ano}")
            resp = input("Deseja fazer outro cálculo? (s/n): ")
            if resp == "n":
                break