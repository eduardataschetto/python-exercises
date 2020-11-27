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


def custo(valor: float, litros: float, litros_necessarios: float, tipo: str) -> list:
    qtd = (litros_necessarios // litros)
    qtd += 1 if litros_necessarios % litros != 0 else 0
    custo = qtd * valor

    return [tipo, custo, qtd]


def custoGalaoLata(litros_necessarios: float) -> list:
    global valor_galao, litros_galao, valor_lata, litros_lata

    # computando a quantidade de latas necessárias
    count_lata = litros_necessarios // litros_lata
    custo_lata = count_lata * valor_lata

    resto = litros_necessarios % litros_lata

    # computando a quantidade de galões necessáris
    count_galao = resto // litros_galao
    count_galao += 1 if resto % litros_galao > 0 else 0
    custo_galao = count_galao * valor_galao

    # calculando o custo total
    custo_total = custo_lata + custo_galao

    return[count_lata, custo_lata, count_galao, custo_galao, custo_total]


def main():
    global valor_galao, litros_galao, valor_lata, litros_lata
    while True:
        try:
            m = float(input("Informe o tamanho da área a ser pintada (m²): "))
            if m < 0:
                continue
            break
        except ValueError:
            print("Valor inválido! Tente novamente. ")

    tinta_necessaria = (m / 6) * 1.1

    latas = custo(valor_lata, litros_lata, tinta_necessaria, "LATAS - 18L")
    galoes = custo(valor_galao, litros_galao,
                   tinta_necessaria, "GALÕES - 3.6L")
    lata_galao = custoGalaoLata(tinta_necessaria)

    # imprimindo orçamento para latas e galões
    for i in [latas, galoes]:
        print(
            f"\n\tORÇAMENTO PARA {i[0]}\n\tCUSTO: {i[1]}\n\tQUANTIDADE: {int(i[2])}\n")

    # imprimindo orçamento para a mistura de latas e galões
    print(f"""\tORÇAMENTO PARA LATAS E GALÕES: 
        QUANTIDADE DE LATAS: {int(lata_galao[0])}
        CUSTO LATAS: {lata_galao[1]}
        QUANTIDADE DE GALÕES: {int(lata_galao[2])}
        CUSTO GALÕES: {lata_galao[3]}
        CUSTO TOTAL: {lata_galao[4]}
    """)


if __name__ == "__main__":
    main()
    while True:
        op = input("Deseja executar novamente? [S/N] ").upper()

        if op in 'SN':
            if op == 'S':
                limpaTela()
                main()
            else:
                break
