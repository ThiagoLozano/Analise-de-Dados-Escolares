# PROJETO PYTHON: Análise De Notas Escolares

> Um sistema que abre um arquivo .CSV direto do console e retorna funções com análises obtidas do arquivo.

 O programa deve ler um arquivo CSV contendo as colunas RA, P1, P2 e Trabalho. Ao ler o arquivo, o programa 
deve retornar algumas análises como: 
- Total de Alunos Registrados;
- A média de cada aluno;
- A média total da sala;
- Mostrar alunos que precisarão de recuperação;

Se o programa não encontrar o arquivo CSV ele deve retornar uma mensagem de erro.

# Tecnologias Utilizadas
* **_PyCharm;_**
* **_Python 3;_**

# Exemplo de Uso
### Arquivo CSV Criado.
```
RA, Nome, P1, P2, Trabalho
12345678, Aluno A, 10.0, 7.5, 8.0
87654321, Aluno B, 9.0, 8.5, 5.5
12345698, Aluno C, 8.7, 6.5, 4.0
45679813, Aluno D, 6.5, 4.5, 10.0
79876461, Aluno E, 4.5, 7.5, 8.5
79843213, Aluno F, 3.5, 6.5, 7.3
75389413, Aluno G, 8.4, 6.7, 7.8
54618654, Aluno H, 9.6, 4.5, 8.8
23135468, Aluno I, 6.5, 4.5, 8.8
68468464, Aluno J, 4.3, 4.5, 6.5
```
![CSV](https://github.com/ThiagoLozano/Analise-de-Dados-Escolares/blob/master/Screenshot/CSV.PNG)


### Função que retorna a média final de todos os alunos.
```
@staticmethod
    def MediaAlunos(doc):
        print('=' * 45)
        print('Média final de Todos os Alunos:')
        # Cria a coluna 'Média'.
        doc['Média'] = round((doc['P1'] + doc['P2'] + doc['Trabalho']) / 3, 1)
        # Retorna o nome do aluno e sua média correspondente.
        print(doc[['Nome', 'Média']])
```
![Função Média Final](https://github.com/ThiagoLozano/Analise-de-Dados-Escolares/blob/master/Screenshot/Funcao.PNG)

# Bibliotecas e Configurações

### Biblioteca Python Utilizada.

```
import pandas as pd
```
![Biblioteca](https://github.com/ThiagoLozano/Analise-de-Dados-Escolares/blob/master/Screenshot/Biblioteca.PNG)
