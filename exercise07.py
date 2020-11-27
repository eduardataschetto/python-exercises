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


def countChar(char:str, phrase:str) -> int:
    new_ph = unicodedata.normalize("NFD", phrase).upper()
    count = new_ph.count(char.upper())

    return count


def main():
    print(f"{'*'*10}  CONTADOR DE ESPAÇOS EM BRANCO E VOGAIS  {'*'*10}\n")
    frase = input("Informe uma frase: ")
    limpaTela()

    print(f"""
    FRASE: {frase}

    NÚMERO DE ESPAÇOS EM BRANCO: {countChar(' ', frase)}

    NÚMERO DE VOGAIS: 
    A: {countChar('a', frase)}
    E: {countChar('e', frase)}
    I: {countChar('i', frase)}
    O: {countChar('o', frase)}
    U: {countChar('u', frase)}
    """)



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
