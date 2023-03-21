matriz_coeficientes = [
    [4, -2, 3, 23],
    [9, 3, -7, -7],
    [2, 1, -4, -17]
]


def imprime_matriz(matriz):
    linha = len(matriz)
    coluna = len(matriz[0])
    index_linhas = 0
    index_coeficientes = 0
    saida = ""

    while index_linhas < linha:
        while index_coeficientes < coluna:
            saida += str(matriz[index_linhas][index_coeficientes])+" "
            index_coeficientes += 1
        saida += "\n"
        index_linhas += 1
        index_coeficientes = 0

    print(saida)


def recalculaLinha(linha, valor_diagonal):
    tamanho = len(linha)
    index = 0

    while index < tamanho:
        linha[index] = round(linha[index] / valor_diagonal, 2)
        index += 1

    return linha


def valor_diagonal(matriz):
    linhas = len(matriz)
    indice_linhas = 0
    indice_coeficientes = 0
    numero_coeficiente = len(matriz[0])

    while indice_linhas < linhas:
        while indice_coeficientes < numero_coeficiente:
            # Testa se é valor diagonal
            if (indice_linhas == indice_coeficientes):
                valor_diagonal = matriz[indice_linhas][indice_coeficientes]
            indice_coeficientes += 1
        # Terminei de ler os valores da linha
        linha = matriz[indice_linhas]
        matriz[indice_linhas] = recalculaLinha(linha, valor_diagonal)

        indice_coeficientes = 0
        indice_linhas += 1

    imprime_matriz(matriz)


valor_diagonal(matriz_coeficientes)
