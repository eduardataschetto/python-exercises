# construa um analisador das 5 principais combinações de mãos do poker.
# Para isso utilize como base as classes descritas em:
# https://penseallen.github.io/PensePython2e/18-heranca.html
# considere como regra o poker fechado, em que a mão do jogador, já tem a combinação de 5 cartas :)
from __future__ import print_function, division
from os import system, name
from time import sleep
import random


class Carta:

    naipes_nomes = ["Paus", "Ouros", "Copas", "Espadas"]
    valor_names = [None, "Ás", "2", "3", "4", "5", "6", "7",
                   "8", "9", "10", "Valete", "Dama", "Rei"]

    def __init__(self, naipe=0, valor=2):
        self.naipe = naipe
        self.valor = valor

    def __str__(self):
        return '%s de %s' % (Carta.valor_names[self.valor],
                             Carta.naipes_nomes[self.naipe])

    def __eq__(self, other):
        return self.naipe == other.naipe and self.valor == other.valor

    def __lt__(self, other):
        t1 = self.naipe, self.valor
        t2 = other.naipe, other.valor
        return t1 < t2


class Baralho:
    def __init__(self):
        self.cartas = []
        for naipe in range(4):
            for valor in range(1, 14):
                carta = Carta(naipe, valor)
                self.cartas.append(carta)

    def __str__(self):
        res = []
        for carta in self.cartas:
            res.append(str(carta))
        return '\n'.join(res)

    def addCarta(self, carta):
        self.cartas.append(carta)

    def popCarta(self, i=-1):
        return self.cartas.pop(i)

    def shuffle(self):
        random.shuffle(self.cartas)

    def sort(self):
        self.cartas.sort()

    def moveCartas(self, mao, num):
        for i in range(num):
            mao.addCarta(self.popCarta())


class Mao(Baralho):
    def __init__(self, label=''):
        self.cartas = []
        self.label = label

    def getValores(self):
        valores = []

        # gerando lista dos valores das cartas
        for carta in self.cartas:
            valores.append(carta.valor)
        return valores


    def getNaipes(self) -> list:
        naipes = []

        # gerando lista dos naipes das cartas
        for carta in self.cartas:
            naipes.append(carta.naipe)
        return naipes


    def countValoresRepetidos(self) -> list:
        valores = self.getValores()

        # removendo elementos repetidos
        valores_norepeat = []
        for valor in valores:
            if not valor in valores_norepeat:
                valores_norepeat.append(valor)

        # gerando lista contadora de valores repetidos
        count = []
        for valor in valores_norepeat:
            contador = valores.count(valor)
            if contador > 1:
                count.append(contador)
        return sorted(count)


    # falta verificar para a sequencia 10, 11, 12, 13, 1
    def sequencia(self):
        valores = self.getValores()
        valores = sorted(valores)

        anterior = valores[0]
        valores.remove(anterior)
        for valor in valores:
            if valor - 1 == anterior:
                anterior = valor
            else:
                return False
        if not self.flush():
            return True


    def flush(self):
        # resgatando lista com todos os naipes
        naipes = self.getNaipes()

        # verificando se todos são iguais
        if naipes.count(naipes[0]) == 5:
            return True


def main():
    print(f"{'*'*8} ANALISADOR DE COMBINAÇÃO DAS MÃOS DO POKER {'*'*8}\n\n")
    print("Embaralhando as cartas...")
    sleep(1)
    limpaTela()
    print("Dando as cartas...")
    sleep(1.5)
    limpaTela()
    mao = geraMao()
    print(f"{'*'*5} SUAS CARTAS NESSA RODADA {'*'*5}\n")
    print(mao)
    sleep(3)
    print(f"Você pegou {verifica_combinacao(mao)}")


def geraMao() -> object:
    baralho = Baralho()
    baralho.shuffle()
    mao = Mao()
    baralho.moveCartas(mao, 5)
    mao.sort()
    return mao


def verifica_combinacao(mao:object) -> str:
    repetidos = mao.countValoresRepetidos()
    combinacao = ''

    if repetidos.count(2) == 1 and not repetidos.count(3):
        combinacao = ' UM PAR'
    elif repetidos.count(2) == 2:
        combinacao = 'DOIS PARES'
    elif repetidos.count(3) and not repetidos.count(2):
        combinacao = 'TRINCA'
    elif repetidos.count(4):
        combinacao = 'QUADRA'
    elif repetidos.count(3) and repetidos.count(2):
        combinacao = 'FULL HOUSE'
    elif mao.sequencia():
        combinacao = 'SEQUÊNCIA'
    elif mao.flush():
        combinacao = 'FLUSH'
    elif mao.flush() and mao.sequencia():
        combinacao = 'STRAIGHT FLUSH'
    else:
        combinacao = 'nada de interessante. Tente novamente.'

    return combinacao


def limpaTela():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


if __name__ == '__main__':
    main()
    while True:
        op = input("Deseja jogar novamente? [S/N] ").upper()

        if op in 'SN':
            if op == 'S':
                limpaTela()
                main()
            else:
                break
