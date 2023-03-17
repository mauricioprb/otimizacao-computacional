import re

nomes_variaveis = {}


def retorna_coeficiente(linha, pos):


valor = []
pc = pos - 1
while pc >= 0:
if linha[pc] == '+' or linha[pc] == '-':
if linha[pc] == '-':
valor.append(linha[pc])
if len(valor) == 1:
valor.insert(0, '1')
break
else:
if len(valor) == 0:
valor.append('1')
break
valor.append(linha[pc])
pc = pc - 1
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
coef = coef + letra
indice += 1
else:
if indice == 0:
coef = '1'
variavel = termo[indice:]
break
return coef, variavel


def monta_coeficientes(linha_entrada):


nv = nomes_variaveis.keys()
for nome_v in nv:
pos = linha_entrada.find(nome_v)
coef = -100
if pos < 0:
coef = 0
else:
if pos == 0:
coef = 1
else:
if pos == 1:
if linha_entrada[pos-1] == '-':
coef = -1
else:
coef = int(linha_entrada[pos-1])
else:
coef = retorna_coeficiente(linha_entrada, pos)
print(nome_v, ':', pos, ' c:', coef)


def busca_valores(dados_valores):


print(nomes_variaveis.keys())
for l in dados_valores:
print('Linha entrada:', l)
monta_coeficientes(l)


def abre_arquivo(nome_arquivo):


dados = open(nome_arquivo)
dados_valores = []
for linha in dados:
print(linha)
linha = linha.replace(' ', '')
dados_valores.append(linha)
elementos = linha.split('=')
le = elementos[0]
ld = elementos[1]
termos = re.split('-|+', le)
for termo in termos:
if len(termo) > 0:
c, v = separa_coef_var(termo.lstrip().rstrip())
insere_variavel(v)
return dados_valores

lst = abre_arquivo(
    '/content/drive/MyDrive/2023/1 SEMESTRE/Otimizacao/equacoes.txt')
busca_valores(lst)
c, v = separa_coef_var('x1')
print('Coeficiente:', c, 'Variavel:', v)
