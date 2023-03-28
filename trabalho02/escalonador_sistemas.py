import re

matriz = []
nome_variaveis = {}  # Dicionário com o nome das variáveis


def escalonar(matriz, chaves):
    linhas = len(matriz)
    colunas = len(matriz[0])

    for i in range(linhas):
        # Encontrar o pivo
        pivo = matriz[i][i]
        # Fazer o elemento na diagonal principal igual a 1
        if pivo != 1:
            for j in range(colunas):
                matriz[i][j] /= pivo
        # Zerar os elementos acima e abaixo da diagonal principal
        for j in range(linhas):
            if j != i:
                #  Fator de escala que é igual ao elemento na coluna do pivô dividido pelo pivô da linha que contém o pivô
                fator = matriz[j][i]
                # Garante que todos os elementos abaixo e acima da diagonal principal sejam iguais a zero
                for k in range(colunas):
                    # Subtrai o produto desse fator de escala pelo elemento na coluna do pivô da linha que contém o pivô de cada elemento na linha atual
                    matriz[j][k] -= fator * matriz[i][k]
    # Arredonda elementos para duas casas decimais
    matriz = [[round(elem, 2) for elem in row] for row in matriz]
    # Exibe valores das variáveis
    lista = []

    for sublista in matriz:
        ultimo_elemento = sublista[-1]
        lista.append(ultimo_elemento)

    for i in matriz:
        print(i)

    for variavel, resultado in zip(chaves, lista):
        print(variavel, '=', resultado)


def retorna_coeficiente(linha, pos):
    valor = []
    pc = pos-1

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
        pc = pc-1  # Andar para a esquerda

    valor.reverse()

    return ''.join(valor)


def insere_variavel(variavel):
    if variavel not in nome_variaveis:
        nome_variaveis[variavel] = 'sim'


def separa_coeficiente_variavel(termo):
    coef = ''
    variavel = ''
    indice = 0

    for letra in termo:
        if (letra.isdigit()):
            coef = coef+letra
            indice += 1  # Incrementa o índice
        else:
            if indice == 0:  # A primeira letra não é número
                coef = '1'
            variavel = termo[indice:]
            break  # Sai do for

    return coef, variavel

# Monta um vetor com os coeficientes das keys a partir da linha


lista_coeficientes = []


def monta_coeficientes(linha_entrada, chaves):
    # `global` para mostrar que é a mesma variável que estamos usando 'globalmente'
    global matriz
    global lista_coeficientes

    nv = nome_variaveis.keys()
    lista_coeficientes_linha = []

    # Procurar cada nome de variável em todas as linhas
    for nome_variavel in nv:  # Cada nome de variável entre todas
        pos = linha_entrada.find(nome_variavel)
        coef = -100
        if pos < 0:  # Nome variável não encontrado na linha
            coef = 0
        else:
            if pos == 0:  # Nome variável foi encontrado no início da linha
                coef = 1
            else:
                if pos == 1:  # Nome da variável está na posição 1
                    if linha_entrada[pos-1] == '-':
                        coef = -1
                    else:
                        coef = float(linha_entrada[pos-1])
                else:  # O nome da variável está na posição > 1
                    # tratamento do coeficiente
                    coef = retorna_coeficiente(linha_entrada, pos)

        # Armazena os coeficientes da linha
        lista_coeficientes_linha.append(coef)
    # Agrupa todos os coeficientes da linha
    lista_coeficientes.append(lista_coeficientes_linha)
    # Atribui a lista de coeficientes a variável matriz
    matriz = lista_coeficientes

    # Conveter os elementos para int
    for linha in matriz:
        # Percorre cada elemento da linha e converte para int
        for i in range(len(linha)):
            linha[i] = float(linha[i])

    # Insere as chaves na posição inicial da matriz
    return matriz


def buscar_valores(dados_valores, chaves, ld):
    lista_int = list(map(int, ld))

    for i, l in enumerate(dados_valores):  # Para cada linha e elemento da lista ld
        # Cria uma matriz com os coeficientes da linha
        resultado = monta_coeficientes(l, chaves)
        # Adiciona cada elemento dentro de cada lista de linha
        resultado[i].append(lista_int[i])

    # Insere as chaves na posição inicial da matriz
    escalonar(matriz, chaves)


def abre_arquivo(nome_arquivo):
    dados = open(nome_arquivo)
    dados_valores = []
    ld = []

    for linha in dados:  # Percorre linha a linha o arquivo
        linha = linha.rstrip()
        linha = linha.replace(' ', '')  # Tira espaco em branco
        dados_valores.append(linha)
        elementos = linha.split('=')  # Quebra a linha no igual
        le = elementos[0]
        lado_direito = elementos[1]
        ld.append(lado_direito)
        termos = re.split('-|\+', le)

        for termo in termos:
            if len(termo) > 0:
                c, v = separa_coeficiente_variavel(termo.lstrip().rstrip())
                insere_variavel(v)

    # Obtém uma lista de todas as chaves do dicionário
    chaves = list(nome_variaveis.keys())
    # Adiciona as chaves não existentes na lista de chaves
    chaves += [v for v in nome_variaveis.keys() if v not in chaves]

    return dados_valores, chaves, ld


lst, ch, ld = abre_arquivo('trabalho02\equacoes.txt')
buscar_valores(lst, ch, ld)
