"""
5.	Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:
-	A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
-	A mensagem "Reprovado", se a média for menor do que sete;
-	A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""

nota1 = input("Digite a primeira nota: ")
nota2 = input("Digite a segunda nota: ")
media = (int(nota1) + int(nota2))/2

if int(media) >= 7 and int(media) <= 9:
    print(f"Aprovado com média: {media}")
if int(media) < 7:
    print(f"Reprovado com média: {media}")
if int(media) == 10:
    print(f"Aprovado com Distinção")