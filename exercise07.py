# Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

#     quantos espaços em branco existem na frase.
#     quantas vezes aparecem as vogais a, e, i, o, u.


from os import system, name
import unicodedata


def limpaTela():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def countChar(char:str, phrase:str) -> list:
    new_ph = unicodedata.normalize("NFD", phrase)
    count = 0
    for c in char.upper():
        for i in new_ph.upper():
            if i == c:
                count += 1
    return count


def main():
    print(f"{'*'*10}  CONTADOR DE ESPAÇOS EM BRANCO E VOGAIS  {'*'*10}\n")
    frase = input("Informe uma frase: ")

    print(f"FRASE: {frase}\nNÚMERO DE ESPAÇOS EM BRANCO: {countChar(' ', frase)}\nNÚMERO DE VOGAIS: {countChar('aeiou', frase)}")


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

# Gostei bastante da sua lógica
# você usou umas bibliotecas diferentes, vou ate dar uma pesquisada sobre elas
# ademais o código aparenta estar muito bom