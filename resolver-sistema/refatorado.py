import re  # Módulo para expressões regulares

nomes_variaveis = {}  # Dicionário com o nome das variáveis


def retorna_coeficiente(linha, pos):
    valor = []
    pc = pos-1
    while pc >= 0:
        if linha[pc] == '+' or linha[pc] == '-':
            if linha[pc] == '-':
                valor.append(linha[pc])  # Adiciona '-' ao valor
                if len(valor) == 1:
                    valor.insert(0, '1')  # Adiciona '1' antes do '-'
                break
            else:
                if len(valor) == 0:
                    valor.append('1')
                break
        valor.append(linha[pc])
        pc -= 1  # move-se para a esquerda
    valor.reverse()
    return ''.join(valor)


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
            if indice == 0:  # A primeira letra não é um número
                coef = '1'
            variavel = termo[indice:]
            break
    return coef, variavel


def monta_coeficientes(linha_entrada):
    variaveis = nomes_variaveis.keys()
    for nome_variavel in variaveis:
        pos = linha_entrada.find(nome_variavel)
        coef = -100
        if pos < 0:  # Nome de variável não encontrado na linha
            coef = 0
        else:
            if pos == 0:  # Nome de variável encontrado no início da linha
                coef = 1
            else:
                if pos == 1:  # Nome de variável está na posição 1
                    if linha_entrada[pos-1] == '-':
                        coef = -1
                    else:
                        coef = int(linha_entrada[pos-1])
                else:  # o nome da variável está na posição > 1
                    # tratamento do coeficiente
                    coef = retorna_coeficiente(linha_entrada, pos)
            print(nome_variavel, ':', pos, ' c:', coef)


def abre_arquivo(nome_arquivo):
    dados = open(nome_arquivo)
    for linha in dados:  # Percorre linha a linha o arquivo
        print(linha)
        elementos = linha.split('=')  # Quebra a linha no igual
        lado_esquerdo = elementos[0]
        lado_direito = elementos[1]
        termos = re.split('-|\+', lado_esquerdo)
        for termo in termos:
            if len(termo) > 0:
                c, v = separa_coef_var(termo.strip())
                insere_variavel(v)
        monta_coeficientes(linha)


abre_arquivo('resolver-sistema/equacoes.txt')
c, v = separa_coef_var('x1')
print('Coeficiente: ', c, 'Variável:', v)
