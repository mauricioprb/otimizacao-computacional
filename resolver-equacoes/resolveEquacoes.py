import re  # Expressão regular

matriz = []
nomesVariaveis = {}  # Dicionário com o nome das variaveis


def retornaCoefiente(linha, pos):
    valor = []
    pc = pos - 1
    while pc >= 0:
        if linha[pc] == '+' or linha[pc] == '-':
            if linha[pc] == '-':
                valor.append(linha[pc])  # Fez append com o '-'
                if len(valor) == 1:
                    valor.insert(0, '1')
                break
            else:
                if len(valor) == 0:
                    valor.append('1')
                break
        valor.append(linha[pc])
        pc = pc - 1  # Andar para a esquerda
    valor.reverse()
    return ''.join(valor)


def insereVariavel(variavel):
    if variavel not in nomesVariaveis:
        nomesVariaveis[variavel] = 'sim'


def separaCoef_var(termo):
    coef = ''
    variavel = ''
    indice = 0
    for letra in termo:
        if (letra.isdigit()):
            coef = coef + letra
            indice += 1  # Incrementa o índice
        else:
            if indice == 0:  # A primeira letra nao eh numero
                coef = '1'
            variavel = termo[indice:]
            break  # Sai do for
    return coef, variavel

# Monta um vetor com os coeficientes das
# Keys a partir da linha


listaCoeficientes = []


def montaCoeficientes(linha_entrada, chaves):
    # Usamos o `global` para mostrar que é a mesma variavel que estamos usando 'globalmente'
    global matriz
    global listaCoeficientes
    nv = nomesVariaveis.keys()
    listaCoeficientesLinha = []

    # Vamos procurar cada nome de variavel em TODAS as linhas
    for nomeV in nv:  # cada nome de variavel entre todas.
        pos = linha_entrada.find(nomeV)
        coef = - 100
        if pos < 0:  # Nome variavel nao encontrado na linha
            coef = 0
        else:
            if pos == 0:  # Nome variavel foi encontrado no inicio da linha
                coef = 1
            else:
                if pos == 1:  # Nome da variavel esta posicao 1
                    if linha_entrada[pos - 1] == '-':
                        coef = -1
                    else:
                        coef = float(linha_entrada[pos - 1])
                else:  # O nome da variavel esta na posicao >1
                    # Tratamento do coeficiente
                    coef = retornaCoefiente(linha_entrada, pos)
        # Armazena os coeficientes da linha
        listaCoeficientesLinha.append(coef)
    # Agrupa todos os coeficientes da linha
    listaCoeficientes.append(listaCoeficientesLinha)
    # Atribui a lista de coeficientes a variável matriz
    matriz = listaCoeficientes
    # Conveter os elementos para INT
    for linha in matriz:
        # Percorre cada elemento da linha e converte para int
        for i in range(len(linha)):
            linha[i] = float(linha[i])
    # Insere as chaves na posição inicial da matriz
    return matriz


def buscaValores(dadosValores, chaves, ld):
    lista_int = list(map(int, ld))
    for i, l in enumerate(dadosValores):  # Para cada linha e elemento da lista ld
        # Cria uma matriz com os coeficientes da linha
        resultado = montaCoeficientes(l, chaves)
        # Adiciona o elemento da lista ld_list após a matriz
        resultado[i].append(lista_int[i])
    # Insere as chaves na posição inicial da matriz
    matriz.insert(0, chaves)
    for i in matriz:
        print(i)


def diagonal_principal(matriz):
    linhas = len(matriz)  # Número de linhas
    colunas = len(matriz[0])  # Número de colunas
    i = 0
    while i < linhas:
        # Dividir a linha i pelo elemento da diagonal principal
        pivo = matriz[i][i]
        j = 0
        while j < colunas:
            matriz[i][j] /= pivo
            j += 1
        # Zerar todos os elementos abaixo da diagonal principal da coluna i
        k = i + 1
        while k < linhas:
            multiplicador = matriz[k][i]
            j = 0
            while j < colunas:
                matriz[k][j] -= multiplicador * matriz[i][j]
                j += 1
            k += 1
        i += 1
    return matriz


def abre_arquivo(nomeArquivo):
    dados = open(nomeArquivo)
    dadosValores = []
    ld = []
    for linha in dados:  # Percorre linha a linha o arquivo
        linha = linha.rstrip()
        linha = linha.replace(' ', '')  # Tira espaco em branco
        dadosValores.append(linha)
        elementos = linha.split('=')  # Quebra a linha no igual
        le = elementos[0]
        lado_direito = elementos[1]
        ld.append(lado_direito)
        termos = re.split('-|\+', le)
        for termo in termos:
            if len(termo) > 0:
                c, v = separaCoef_var(termo.lstrip().rstrip())
                insereVariavel(v)
    # Obtém uma lista de todas as chaves do dicionário
    chaves = list(nomesVariaveis.keys())
    # Adiciona as chaves não existentes na lista de chaves
    chaves += [v for v in nomesVariaveis.keys() if v not in chaves]
    # print('chaves: ', chaves)
    return dadosValores, chaves, ld


lst, ch, ld = abre_arquivo('resolver-equacoes\equacoes.txt')
buscaValores(lst, ch, ld)
