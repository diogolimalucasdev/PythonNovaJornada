"""
Primeiro de tudo vou fazer a instalação de um modulo PyMysql
pip install pymysql
"""
import pymysql.cursors
from contextlib import contextmanager

"""
Starto meu servior mysql  utilizando o xamp
"""

"to criando uma função para conextar e vou usar o contextmanager"


@contextmanager
def conecta():
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='miguel25082009',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        yield conexao

    finally:
        print('conexao fechada')
        conexao.close()


'fazer o crud da base de dados'
'insere um registro na base de dados'
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES (%s, %s, %s, %s)'
#         cursor.execute(sql, ('Diogo', 'Lima', 21, 53.8))
#         conexao.commit()

'INSERE varios registros na base de dados'
'fazendo a inserção de varios dados de uma vez no meu banco de dados'
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES (%s, %s, %s, %s)'
#
#         # uso o executemany para enviar varios valores, por isso estou criando a lista
#         dados = [
#             ('MURIEL', 'FIGUEREDO', 19, 90.5),
#             ('ROUSE', 'ALBERTO', 44, 45.5),
#             ('ALISSON', 'TORRES', 33, 78.5),
#         ]
#         cursor.executemany(sql, dados)
#         conexao.commit()

'deleta um registro na base de dados'
# 'deletando um id '
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         # deletando o id 7
#         sql = 'DELETE FROM clientes WHERE id = %s'
#         cursor.execute(sql, (7,))
#         conexao.commit()

'deleta quantidades determinada de registro'
'deletando 3 id do banco'
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         # deletando o id 7
#         sql = 'DELETE FROM clientes WHERE id IN (%s, %s, %s)'
#         cursor.execute(sql, (6,8,9))
#         conexao.commit()

'deleta registro entre um range'
'deletando id entre os valores que eu mandar, por exemplo entre 10 e 12, ou seja o 10, 11 e o 12 serao deletados'
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         # deletando o id 7
#         sql = 'DELETE FROM clientes WHERE id BETWEEN %s AND %s'
#         cursor.execute(sql, (10, 12))
#         conexao.commit()

'Atualiza um registro na base de dados'
'atualizando nome dos clientes na minha base de dados'
with conecta() as conexao:
    with conexao.cursor() as cursor:
        # deletando o id 7
        sql = 'UPDATE clientes SET nome=%s WHERE id=%s'
        cursor.execute(sql, ('JOAO', 5))
        conexao.commit()

'este seleciona os dados na base de dados'
'meu primeiro gerenciador de contexto fecha a conexao'
with conecta() as conexao:
    # ja esse segundo gerenciador ta fechando o cursor
    with conexao.cursor() as cursor:
        # posso pegar apenas o nome e sobrenome da minha tabela se eu preferir
        # sempre bom dar limit para consultas sql
        # cursor.execute('SELECT nome, sobrenome FROM clientes LIMIT 100')

        # tambem posso apelidar
        # cursor.execute('SELECT nome as n, sobrenome as sbr FROM clientes')

        # aqui eu estou colocando um limite de ate 100, na minha consulta e ordenando pelo id
        cursor.execute('SELECT * FROM clientes  ORDER BY id ASC LIMIT 100')
        resultado = cursor.fetchall()

        for linha in resultado:
            print(linha)
