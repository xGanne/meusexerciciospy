""" 7.	Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário."""

lado = input("Escreva o tamanho do lado do quadrado: ")
area = int(lado) * int(lado)
area2 = int(area) * 2

print(f"A área do quadrado é: {area}")
print(f"O dobro da área do quadrado é: {area2}")