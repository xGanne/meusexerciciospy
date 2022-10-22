"""
3.	Faça um programa que leia e valide as seguintes informações:
    a.	Nome: maior que 3 caracteres;
    b.	Idade: entre 0 e 150;
    c.	Salário: maior que zero;
    d.	Sexo: 'f' ou 'm';
    e.	Estado Civil: 's', 'c', 'v', 'd';

"""

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
salario = input("Digite seu salário: ")
sexo = input("Digite seu sexo (F/M): ")
estado = input("Digite seu estado civil\n- S = Solteiro(a)\n- C = Casado(a)\n- V = Viúvo(a)\n- D = Divorciado(a): ")

while len(nome) < 3:
    print("Erro encontrado no cadastro das informações, tente novamente.")
    print("--------------------------------------------------------------------------")
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    salario = input("Digite seu salário: ")
    sexo = input("Digite seu sexo (F/M): ")
    estado = input("Digite seu estado civil\n- S = Solteiro(a)\n- C = Casado(a)\n- V = Viúvo(a)\n- D = Divorciado(a): ")

while int(idade) < 0:
    print("Erro encontrado no cadastro das informações, tente novamente.")
    print("--------------------------------------------------------------------------")
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    salario = input("Digite seu salário: ")
    sexo = input("Digite seu sexo (F/M): ")
    estado = input("Digite seu estado civil\n- S = Solteiro(a)\n- C = Casado(a)\n- V = Viúvo(a)\n- D = Divorciado(a): ")

while int(idade) > 150:
    print("Erro encontrado no cadastro das informações, tente novamente.")
    print("--------------------------------------------------------------------------")
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    salario = input("Digite seu salário: ")
    sexo = input("Digite seu sexo (F/M): ")
    estado = input("Digite seu estado civil\n- S = Solteiro(a)\n- C = Casado(a)\n- V = Viúvo(a)\n- D = Divorciado(a): ")

while int(salario) < 0:
    print("Erro encontrado no cadastro das informações, tente novamente.")
    print("--------------------------------------------------------------------------")
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    salario = input("Digite seu salário: ")
    sexo = input("Digite seu sexo (F/M): ")
    estado = input("Digite seu estado civil\n- S = Solteiro(a)\n- C = Casado(a)\n- V = Viúvo(a)\n- D = Divorciado(a): ")

while sexo != "F" and sexo != "M":
    print("Erro encontrado no cadastro das informações, tente novamente.")
    print("--------------------------------------------------------------------------")
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    salario = input("Digite seu salário: ")
    sexo = input("Digite seu sexo (F/M): ")
    estado = input("Digite seu estado civil\n- S = Solteiro(a)\n- C = Casado(a)\n- V = Viúvo(a)\n- D = Divorciado(a): ")

while estado != "S" and estado != "C" and estado != "V" and estado != "D":
    print("Erro encontrado no cadastro das informações, tente novamente.")
    print("--------------------------------------------------------------------------")
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    salario = input("Digite seu salário: ")
    sexo = input("Digite seu sexo (F/M): ")
    estado = input("Digite seu estado civil\n- S = Solteiro(a)\n- C = Casado(a)\n- V = Viúvo(a)\n- D = Divorciado(a): ")