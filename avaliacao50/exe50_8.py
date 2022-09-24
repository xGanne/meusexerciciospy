"""
8) Tabuada de acordo com a escolha do cliente e ao final perguntar se ele deseja uma nova tabuada
"""
num = input("Escreva o número: ")
tabuada = 0
op = "t"
aux = 0

while tabuada <= 8:
    tabuada += 1
    print(f"{num} x {tabuada} = {int(num) * int(tabuada)}")

    if tabuada == 9:
        op = input("Deseja continuar? (s/n): ")

        if op == "s":
            tabuada = int(aux)
            num = input("Escreva o número: ")
            tabuada += 1
            print(f"{num} x {tabuada} = {int(num) * int(tabuada)}")
