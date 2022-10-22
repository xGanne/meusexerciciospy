"""
3.	Faça um Programa que verifique se uma letra digitada é "F" ou "M".
 Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""
resp = input("Escreva seu sexo (F/M): ")

if resp == 'F':
    print("Seu sexo é feminino.")
if resp == 'M':
    print("Seu sexo é masculino.")
if resp != 'F' and resp != 'M':
    print("Sexo inválido.")