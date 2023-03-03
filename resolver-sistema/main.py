import re

nomes_variaveis = {}

def insere_variavel(variavel):
    if variavel not in nomes_variaveis:
        nomes_variaveis[variavel] = 'sim'

def separa_coef_var(termo):
    coef = ''
    variavel = ''
    indice = 0
    for letra in termo:
        if letra.isdigit():
            coef += letra
            indice += 1
        else:
            if indice == 0:
                coef = '1'
            variavel = termo[indice:]
            break
    return coef, variavel

def abre_arquivo(nome_arquivo):
    with open(nome_arquivo) as dados:
        for linha in dados:
            print(linha)
            elementos = linha.split('=')
            le = elementos[0]
            ld = elementos[1]
            if '-' in le and '+' in le:
                termos = re.split('-|\+', le)
                for termo in termos:
                    print('***', termo)
                    c, v = separa_coef_var(termo)
                    insere_variavel(v)
            elif '+' in le:
                variaveisP = le.split('+')
                print('Variaveis (+)->', variaveisP[0], '|', variaveisP[1])
                for variavel in variaveisP:
                    c, v = separa_coef_var(variavel)
                    insere_variavel(v)
            elif '-' in le:
                variaveisN = le.split('-')
                if len(variaveisN) == 2:
                    print('Variaveis (-)->', variaveisN[0], '|', variaveisN[1])
                    for variavel in variaveisN:
                        c, v = separa_coef_var(variavel)
                        insere_variavel(v)
                elif len(variaveisN) == 3:
                    print('Variaveis (-)->', variaveisN[1], '|', variaveisN[2])
                    for variavel in variaveisN[1:]:
                        c, v = separa_coef_var(variavel)
                        insere_variavel(v)
            print(list(nomes_variaveis.keys()))

abre_arquivo('resolver-sistema\equacoes.txt')
c, v = separa_coef_var('x1')
print('Coeficiente:', c, 'Variável:', v)