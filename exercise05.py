#  Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados. 

from random import randint
from os import system, name


def limpa_tela():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def rand():
    return randint(1, 6)
    
def main():
    resultados = []
    for i in range(1, 100):
        resultados.append(rand())

    for i in range(1, 7):
        print(f"\t{i}: {resultados.count(i)}")

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
    
# uma dica seria de colacar no print o que cada valor seria, ficaria mais fácil de entender
# mas o código está muito bom 