import pandas as pd


class Alunos:
    @staticmethod
    def TotalAlunos(doc):
        # Conta o número de registros.
        total = doc['RA'].count()
        print('Total de Alunos Registrados: {}'.format(total))

    @staticmethod
    def MediaAlunos(doc):
        print('=' * 45)
        print('Média final de Todos os Alunos:')
        # Cria a coluna 'Média'.
        doc['Média'] = round((doc['P1'] + doc['P2'] + doc['Trabalho']) / 3, 1)
        # Retorna o nome do aluno e sua média correspondente.
        print(doc[['Nome', 'Média']])

    @staticmethod
    def MediaSala(doc):
        print('=' * 45)
        # Cria um Contador.
        contador = doc['Média'].count()
        # Soma todas as Médias individuais.
        soma = sum(doc['Média'])
        # Cria a media total.
        media = round(soma / contador, 1)
        print('Média de Desempenho da Sala: {}'.format(media))

    @staticmethod
    def Recuperacao(doc):
        print('=' * 45)
        print('Alunos que precisarão fazer a P3:')
        # Pega as médias que são menores que 6.0.
        doc_med = doc[doc['Média'] < 6.0]
        # Retorna o nome e a Média dos Alunos correspondente.
        print(doc_med[['Nome', 'Média']])

    def AbrirArquivo(self):
        try:
            # Abre o arquivo CSV.
            arq = pd.read_csv('nota_alunos.csv', sep=r'\s*,\s*', header=0, encoding='ascii', engine='python')
            print('=' * 45)
            print(arq)
            print('=' * 45)
            # Chama as funções
            self.TotalAlunos(arq)
            self.MediaAlunos(arq)
            self.MediaSala(arq)
            self.Recuperacao(arq)
        except FileNotFoundError:
            print('Erro: Arquivo não encontrado no Diretório.')


user = Alunos()
user.AbrirArquivo()
