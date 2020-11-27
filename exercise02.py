# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

#     Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#     comprar apenas latas de 18 litros;
#     comprar apenas galões de 3,6 litros;
#     misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
from os import system, name


valor_galao, litros_galao = 25.00, 3.6
valor_lata, litros_lata = 80.00, 18


def limpaTela():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def custo(valor:float, litros:float, litros_necessarios:float) -> float:
    custo = (litros_necessarios // litros) * valor
    custo += valor if litros_necessarios % litros != 0 else 0
    return custo


def custoGalaoLata(litros_necessarios:float) -> float:
    global valor_galao, litros_galao, valor_lata, litros_lata
    count_lata = litros_necessarios // litros_lata
    y = litros_necessarios % litros_lata
    count_galao = y // litros_galao
    custo = count_lata * valor_lata + count_galao * valor_galao
    custo += valor_galao if y % litros_galao > 0 else 0
    return custo


def main():
    global valor_galao, litros_galao, valor_lata, litros_lata
    while True:
        try:
            m = float(input("Informe o tamanho da área a ser pintada (m²): "))
            if m < 0:
                continue
        except ValueError:
            print("Valor inválido! Tente novamente. ")

        tinta_necessaria = (m / 6) * 1.1

        custo_lata = custo(valor_lata, litros_lata, tinta_necessaria)
        custo_galão = custo(valor_galao, litros_galao, tinta_necessaria)
        custo_lata_galao = custoGalaoLata(tinta_necessaria)

        print(f"M²: {m}\nCUSTO COM GALÕES: {custo_galão:.2f}\nCUSTO COM LATAS: {custo_lata}\nCUSTO MISTURANDO GALÕES E LATAS: {custo_lata_galao}")


if __name__ == "__main__":
    main()
    while True:
        op = input("Deseja executar novamente? [S/N] ").upper()

        if op in ['S', 'N']:
            if op == 'S':
                limpaTela()
                main()
            else:
                break