# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados
# 11% para o Imposto de Renda,
# 8% para o INSS e
# 5% para o sindicato,
# faça um programa que nos dê:

#     salário bruto.
#     quanto pagou ao INSS.
#     quanto pagou ao sindicato.
#     o salário líquido.
#     calcule os descontos e o salário líquido, conforme a tabela abaixo:
#     + Salário Bruto : R$
#     - IR (11%) : R$
#     - INSS (8%) : R$
#     - Sindicato ( 5%) : R$
#     = Salário Liquido : R$


from os import system, name


def limpa_tela():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def calcula_imposto(valor_hora:float, horas_trab):
    descontos = ['IMPOSTO DE RENDA', 0.11, 'INSS', 0.08, 'SINDICATO', 0.05]
    print(f"\n{'*'*10} CALCULO DE IMPOSTOS {'*'*10}\n")

    sal_bruto = valor_hora * horas_trab
    print(f"SALÁRIO BRUTO: R$ {sal_bruto:.2f}")

    desconto_total = 0
    for i in range(0, len(descontos) - 1, 2):
        desconto = sal_bruto * descontos[i + 1]
        desconto_total += desconto
        print(f"{descontos[i]}: R$ {desconto:.2f}")

    print(f"SALÁRIO LÍQUIDO: R$ {sal_bruto - desconto_total:.2f}")


def main():
    print("Sistema para cálculo de impostos\n")
    while True:
        try:
            valor_hora = float(input("Informe quanto você ganha por hora: "))
            num_horas = float(input("Informe as horas trabalhadas no mês: "))

            if valor_hora < 0 and num_horas < 0:
                continue
            break
        except ValueError:
            print("Valor inválido! Tente novamente. ")
            continue

    calcula_imposto(valor_hora, num_horas)

if __name__=="__main__":
       main()
       while True:
        op = input("Deseja executar novamente? [S/N] ").upper()

        if op in 'SN':
            if op == 'S':
                limpa_tela()
                main()
            else:
                print("Hasta la vista, baby...")
                break