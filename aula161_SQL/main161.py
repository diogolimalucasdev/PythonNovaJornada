import sqlite3

# criando conexão persistente e dou onome de basededados
conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

"AS LINHAS QUE ESTAO COMENTADAS SAO AS INSERÇOES NO BANCO< ESTAO COMENTADAS PARA NAO INSERIR VALORES DUPLICADOS" \
"SE FOR A PRIMEIRA VEZ, RETIRE O #"

# criando uma tabela usando comandos sql
# criando a coluna id e o tipo dele e a chave
# campo nome que é texto
# e o campo peso que é de ponto flutuante
cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'nome TEXT,'
               'peso REAL'
               ')')

# vamos inserir um registro na tabela agora, nos campo nome e peso os valores
"EXECUTEI ESSE COMANDO NA PRIMEIRA VEZ PARA INSERIR UM VALOR "
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("Diogo Lima", 53.4)')

# to enviando o ponto de interrogação pois estou enviando os valores em um tupla
# faço isso para previnir do sql injection
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Fidel', 40))

# outra mandeira de se fazer, so que agora eu mando uma chave e um valor como um dicionario
# cursor.execute(
#     'INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)',
#     {
#         'nome': 'Miguel Lima',
#         'peso': 40.0
#     }
# )

# essa 3 maneira eu omito minhas chaves, perceba que antes dos values eu nao passo o nome e peso
#  mas passo nos values e tenho que passar o id o nome e o peso
# cursor.execute(
#     'INSERT INTO clientes  VALUES (:id, :nome, :peso)',
#     {
#         'id': None,
#         'nome': 'Laryssa ',
#         'peso': 60.0
#     }
# )

# agora tenho que mandar minha conexao executar o comando de cima
# conexao.commit()


# agora indo ate o id 2 e alterando os valores do mesmo(lembrando que nao altero o valor do id, so o nome e peso)
# eu to passando o novo nome, modificando de fidel para maria, lembrando que eu preciso passar qual o id que irei
# modificar
# cursor.execute(
#     'UPDATE clientes SET nome=:nome WHERE id=:id',
#     {
#         'nome': 'Maria',
#         'id': 2
#     }
# )

agora apagando um valor da base de dados, importante prestar atenção no comando
to mandando apagar da minha tabela clientes o id 2
cursor.execute(
    'DELETE FROM clientes WHERE id=:id',
    {
        'id': 2
    }
)

# e faço o commit para executar
conexao.commit()

# agora to pedindo para meu cursos mostrarr todos os valores da minha tabela
cursor.execute('SELECT * FROM clientes')

# e executo o comando fetchal que vai fazer a busca que eu pedi acima
for linha in cursor.fetchall():
    identificador, nome, peso = linha
    print(identificador, nome, peso)

# busacando na minha tabela de dados onde o peso seja maior que 50
# LEMBRANDO QUE ESSA MANEIRA É A MANEIRA MAIS CERTA DE SE FAZER
print()
print("VEJA QUE AGORA SO TEM QUE PESA ACIMA DE 50 e NAO MSTRAMOS O ID")
cursor.execute('SELECT nome, peso FROM clientes WHERE peso > :peso',
               {
                   'peso': 50
               }
               )
for linha in cursor.fetchall():
    nome, peso = linha
    print(nome, peso)

# sempre é bom fechar a conexao e o cursor
cursor.close()
conexao.close()
