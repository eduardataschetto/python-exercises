# Faça um programa que gera uma lista dos números primos existentes entre 1 e
# um número inteiro informado pelo usuário.


from os import system, name


def limpa_tela():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def gera_primos(incio: int, fim: int) -> list:
    primos = []
    for i in range(incio, fim + 1):
        div = 0
        for j in range(1, i + 1):
            if i % j == 0:
                div += 1
        if div == 2:
            primos.append(i)

    return primos


def main():
    print("Gerando lista de primos entre 1 e N.\n")
    while True:
        try:
            n = int(input("Informe N: "))
        except ValueError as e:
            print(e)
            continue
        primos = gera_primos(1, n)
        print(primos)
        break


if __name__ == "__main__":
    main()
    while True:
        op = input("Deseja gerar uma nova lista de primos? [S/N] ").upper()

        if op in ['S', 'N']:
            if op == 'S':
                limpa_tela()
                main()
            else:
                break

# Gostei da sua lógica, nao tinha conseguido fazer, mas depois de ver o teu código eu acho que consigo fazer agora
# Código muito bom e de fácil entendimento
# Muito bom :)