import re # Importa a biblioteca para expressões regulares (regular expression)

nomesVariaveis = {}

# Função para inserir uma variável no dicionário de nomes de variáveis
def insereVariavel(variavel):
  if variavel not in nomesVariaveis:
    nomesVariaveis[variavel]='sim'

# Função para separar o coeficiente e a variável de um termo da equação
def separaCoef_var(termo):
  coef = ''
  variavel = ''
  indice=0
  for letra in termo:
    if(letra.isdigit()):
      coef=coef+letra
      indice+=1 # Incrementa o índice
    else:
      if indice==0:# A primeira letra não é número
        coef='1'
      variavel = termo[indice:]
      break # Sai do for
  return coef,variavel

# Função para abrir e ler o arquivo
def abre_arquivo(nomeArquivo):
  try:
    with open(nomeArquivo) as dados:
      for linha in dados:# Percorre linha a linha o arquivo
        print(linha)
        elementos = linha.split('=')# Quebra a linha no igual
        le = elementos[0]
        ld = elementos[1]
        termos = re.split('-|\+',le) # Separa a equação em termos
        for termo in termos:
          if len(termo)>0:
            c,v = separaCoef_var(termo)
            insereVariavel(v) # Adiciona a variável no dicionário
          print('t:',termo)
        
        print(nomesVariaveis.keys()) # Imprime as chaves do dicionário de nomes de variáveis

  except FileNotFoundError:
    print("Arquivo não encontrado!")

# Chamada da função para abrir e ler o arquivo
abre_arquivo('resolver-sistema\equacoes.txt')

# Chamada da função separaCoef_var para testar um termo
c,v = separaCoef_var('x1')
print('Coeficiente: ',c,'Variavel:',v)