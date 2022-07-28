"""
sempre que precisamos abrir e fechar alguma coisa precisamoa utilizar o gerenciador de contexto
"""

"ao inves de abrir assim meu e arquivo e trabalhar dessa forma"
# arquivo = open('abc.txt', 'w')
# arquivo.write('Alguma coisa')
# arquivo.close()

"eu faço desse jeito"

"aqui eu to abrindo meu arquivo abc e jogado dentro da variavel arquivo e assim eu trabalho com o gerenciador"
with open('abc.txt', 'w') as arquivo:
    arquivo.write('Alguma coisa')



"criando de uma outra maneira meu gerenciador de arquivo "

class Arquivo:
    def __init__(self, arquivo, modo):
        print('Abrindo arquivo  __init__')
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        print('Retornando arquivo __enter__')
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Fechando arquivo  __exit__')
        self.arquivo.close()

"e aqui eu faço a chamada da minha classe que é meu gerenciador "
with Arquivo('abc.txt', 'w') as arquivo:
    arquivo.write('Alguma coisa')