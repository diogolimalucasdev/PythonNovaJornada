"""
comma Separeted Values - CSV(valores separados por vírgula)
É um formato de dados muito usado em tabelas (excel, google sheets), base de dados, clientes de email, etc...
"""
import csv

with open('clientes.csv', 'r') as arquivo:
    "importando normalmente meu csv"
    # dados = csv.reader(arquivo)

    "importando e transformando em dicionario"
    dados = csv.DictReader(arquivo)

    "for para quando for utilizado o dicionario"
    for dado in dados:
        print(dado['Nome'], dado['Sobrenome'], dado['E-mail'], dado['Telefone'])

    "pular a primeira linha Cabeçalho"
    # next(dados)

    "esse for é para ser utilizado quando a importação for normal"
    # for dado in dados:
    #     print(dado)