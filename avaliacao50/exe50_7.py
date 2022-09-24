"""
7) Receba o nome do aluno, três notas (trab(4), teste(3), prova(5)) e calcule a média ponderada
e exiba a média.
"""

nome = input("Escreva seu nome: ")
trab = input("Escreva sua nota do trabalho: ")
teste = input("Escreva sua nota do teste: ")
prova = input("Escreva sua nota da prova: ")

media = (int(trab) * 4) + (int(teste) * 3) + (int(prova) * 5) / (int(trab) + int(teste) + int(prova))
print("-----------------------------------")
print(f"{nome}, sua média (ponderada) é: {media}")
print("-----------------------------------")