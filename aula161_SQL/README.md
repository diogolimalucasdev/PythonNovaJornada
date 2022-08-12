<h1>Estudando SQL com Python </h1>

<h3>
    Primeiro de tudo faço o import do sqlite2

</h3>

````Python
import sqlite3
````

<h3>
Criando conexão persistente e dou o nome de basededados

</h3>

````Python
conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()
````

<h3>
criando uma tabela usando comandos sql,
criando a coluna id e o tipo dele e a chave,
campo nome que é texto,e o campo peso que é 
de ponto flutuante

</h3>

````Python
cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'nome TEXT,'
               'peso REAL'
               ')')
````

<h2>
Aprendi 4 maneiras de inserir os meus dados

</h2>

<h3>

1º - Maneira, que o professor falou que nao é muito indicado

</h3>


````Python
cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("Diogo Lima", 53.4)')

````

<h3>

2º- Maneira, to enviando o ponto de interrogação pois estou enviando os valores em um tupla,
 faço isso para previnir do sql injection(tenho que pesquisar sobre para entender o que pode causar)

</h3>

````Python
cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Fidel', 40))

````

<h3>

3º- Maneira, o que agora eu mando uma chave e um valor como um dicionario

</h3>

````Python
cursor.execute(
    'INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)',
    {
       'nome': 'Miguel Lima',
         'peso': 40.0
    }
    )

````

<h3>
4º - Maneira, essa 4 maneira eu omito minhas chaves, perceba que antes dos values eu nao passo o nome e peso
mas passo nos values e tenho que passar o id o nome e o peso

</h3>

````Python
cursor.execute(
    'INSERT INTO clientes  VALUES (:id, :nome, :peso)',
    {
        'id': None,
        'nome': 'Laryssa ',
        'peso': 60.0
    }
)

````

<h2>
Agora depois de saber como inserir cada dado, tem o comando de executar que é
</h2>

````Python
conexao.commit()

````

<h2>
Atualizando valores da minha tabela

Agora indo ate o id 2 e alterando os valores do mesmo(lembrando que nao altero o valor do id, so o nome e peso)
eu to passando o novo nome, modificando de fidel para maria, lembrando que eu preciso passar qual o id que irei
modificar

</h2>

````Python
cursor.execute(
    'UPDATE clientes SET nome=:nome WHERE id=:id',
    {
        'nome': 'Maria',
        'id': 2
    }
)

````

<h2> 
Apagando um valor da base de dados, importante prestar atenção no comando
to mandando apagar da minha tabela clientes o id 2

</h2>

````Python
cursor.execute(
    'DELETE FROM clientes WHERE id=:id',
    {
        'id': 2
    }
)

````

<h3>
Lembrando de fazer o commit para executar
</h3>

````Python
conexao.commit()
````

<h3>
To pedindo para meu cursos mostrar todos os valores da minha tabela
</h3>

````Python
cursor.execute('SELECT * FROM clientes')

````

<h3>
E executo o comando fetchal que vai fazer a busca que eu pedi acima
</h3>

````Python

for linha in cursor.fetchall():
    identificador, nome, peso = linha
    print(identificador, nome, peso)
````

<h3>
buscando na minha tabela de dados onde o peso seja maior que 50
LEMBRANDO QUE ESSA MANEIRA É A MANEIRA MAIS CERTA DE SE FAZER

</h3>

````Python
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


````

<h3>
Por ultimo mas muito importante,
fechar a conexao e o cursor
</h3>

````Python

cursor.close()
conexao.close()
````

















