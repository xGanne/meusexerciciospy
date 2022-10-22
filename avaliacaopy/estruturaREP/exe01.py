"""
1.	Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
"""
nota = input("Digite sua nota de 0 a 10: ")

if int(nota) > 0 or int(nota) < 10:
    print(f"Sua nota é: {nota}")

while int(nota) < 0 or int(nota) > 10:
    print("Valor inválido, tente novamente.")
    print("------------------------------------")
    nota = input("Digite sua nota de 0 a 10: ")

    if int(nota) > 0 or int(nota) < 10:
        print(f"Sua nota é: {nota}")