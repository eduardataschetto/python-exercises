# Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:

#    0  - 8  3  4 
#    3  - 1  5  9
#    6  - 6  7  2

# Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3. 


from itertools import permutations

def main():
    print(f"\n{'*'*5} QUADRADOS MÁGICOS DE ORDEM 3x3 {'*'*5}\n")
    quadrados = list(permutations([1,2,3,4,5,6,7,8,9]))

    for q in quadrados:
        soma = q[0] + q[1] + q[2]
        valid = True

        # verifica a soma das linhas
        for i in range(0, 7, 3):
            if (q[i] + q[i + 1] + q[i + 2]) != soma:
                valid = False

        # verifica a soma das colunas
        for i in range(0, 3):
            if (q[i] + q[i + 3] + q[i + 6]) != soma:
                valid = False
            
        # verifica a soma das diagonais
        s = (q[0] + q[4] + q[8])
        ss = (q[2] + q[4] + q[6])
        if s != soma or ss != soma:
            valid = False

        if valid:
            print('[',end=" ")
            for i in range(0, 7, 3):
                print(f"[{q[i]} {q[i + 1]} {q[i + 2]}]", end=" ")
            print(']')


if __name__ == "__main__":
    main()