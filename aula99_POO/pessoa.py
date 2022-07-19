# importar o datetime para pegar o ano atual
from datetime import datetime


# nome de classe em maiuscula
class Pessoa:
    # criando variavel para a classe geral, nao para cada atributo
    ano_atual = int(datetime.strftime(datetime.now() , '%Y'))

    # o self referencia a minha instancia da minha classe que no caso é o p1 e o p2
    def __init__(self , nome , idade , comendo = False , falando = False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

        # posso criar uma variavel dentro desse metodo init, mas ela so é valida aqui dentro
        variavel = 'Valor'
        print(variavel)

    def falar(self , assunto):
        if self.comendo:
            print(f'{self.nome} Nao pode falar comendo!')
            return
        if self.falando:
            print(f'{self.nome} Ja esta falando.')
        print(f'{self.nome} Esta falando sobre {assunto}')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} nao est falando')
            return
        print(f'{self.nome} parou de falar')
        self.falando = False

    def comer(self , alimento):
        # faço um if para nao permitir que a pessoa coma dois alimentos ao mesmo tempo
        if self.comendo:
            print(f'{self.nome} ja esta comendo')
            return
        print(f'{self.nome} esta comendo {alimento}.')

        if self.falando:
            print(f'{self.nome} nao pode comer falando')
            return

        # mudando o status da minha variavel comendo para True
        self.comendo = True

    def parar_comer(self):
        # verifico se a pessoa esta comendo, pois se nao estuver comendo nao tem como pedir pra parar
        if not self.comendo:
            print(f'{self.nome} nao esta comendo.')
            return
        print(f'{self.nome} parou de comer')
        self.comendo = False

    def outro_metodo(self):
        # aqui eu ja nao tenho acesso a minha (variavel = 'valor) que foi criado no init

        # mas posso usar as variaveis criadas  com o self, como exemplo:
        print(self.nome)

    def get_ano_nascimento(self):
        #mesmo ela esta fora de init eu preciso utilizar o self para referenciar minha variavel
        return self.ano_atual - self.idade

# criando um metodo que nada mais é do que um função que pertence a uma classe
# def falar(self):
#     print("Pessoa esta falando...")
