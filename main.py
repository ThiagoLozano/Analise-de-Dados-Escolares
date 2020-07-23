import pandas as pd


def contarAlunos(doc):
    total = doc['RA'].count()
    print('Total de Alunos Registrados: {}'.format(total))


def mostrarMedia(doc):
    print('=' * 45)
    print('Média final de Todos os Alunos:')
    doc['Média'] = round((doc['P1'] + doc['P2'] + doc['Trabalho']) / 3, 1)
    print(doc[['Nome', 'Média']])


def mediaTotal(doc):
    print('=' * 45)
    contador = doc['Média'].count()
    soma = sum(doc['Média'])
    media = round(soma / contador, 1)
    print('Média de Desempenho da Sala: {}'.format(media))


def mostrarRecuperacao(doc):
    print('=' * 45)
    print('Alunos que precisarão fazer a P3:')
    doc_med = doc[doc['Média'] <= 6.0]
    print(doc_med[['Nome', 'Média']])


try:
    arq = pd.read_csv('nota_alunos.csv', sep=r'\s*,\s*', header=0, encoding='ascii', engine='python')
    print('=' * 45)
    print(arq)
    print('=' * 45)
    contarAlunos(arq)
    mostrarMedia(arq)
    mediaTotal(arq)
    mostrarRecuperacao(arq)
except FileNotFoundError:
    print('Erro: Arquivo não encontrado no Diretório.')
