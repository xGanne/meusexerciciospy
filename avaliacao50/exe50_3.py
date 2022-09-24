'3) Receber um nome e 3 notas, calcular a média final, dizer se a média for maior que 7 = aprovado, se não = reprovado'

nome = input("Escreva seu nome: ")
nota1 = input("Digite a primeira nota: ")
nota2 = input("Digite a segunda nota: ")
nota3 = input("Digite a  terceira nota: ")
media = (float(nota1) + float(nota2) + float(nota3)) / 3

if media >= 7.0:
    print(f"Parabéns {nome}, você foi aprovado e sua media foi: {media}")
else:
    print(f"{nome}, infelizmente você foi reprovado e sua media foi: {media}")
