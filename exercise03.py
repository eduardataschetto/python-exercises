# Faça um Programa que peça os 3 lados de um triângulo.
# O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.


from os import system, name


def limpa_tela():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def main():
    while True:
        try:
            a = float(input("Informe o lado A: "))
            b = float(input("Informe o lado B: "))
            c = float(input("Informe o lado C: "))
            break
        except ValueError as e:
            print(e)
            continue

    if a < (b+c) and b < (a+c) and c < (a+b):
        print(f"Os valores {a}, {b} e {c} podem formar um triângulo!")

        if a == b and b == c:
            print("Triângulo Equilátero!")
        elif a == b or b == c or a == c:
            print("Triângulo Isósceles!")
        else:
            print("Triângulo Escaleno!")
    else:
        print(f"Os valores {a}, {b} e {c} não podem formar um triângulo!")
        


if __name__ == "__main__":
    main()
    while True:
        op = input("Deseja executar novamente? [S/N] ").upper()
        if op in 'SN':
            if op == 'S':
                limpa_tela()
                main()
            else:
                break
