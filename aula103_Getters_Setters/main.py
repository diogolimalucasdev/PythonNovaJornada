# getter = Obtem um valor
# setter = COnfigura um valor

# os metodos getters e setters sao uma proteção para o meu atributo, para que nao chegue uma valor fora do padrao
# esperado pelo meu atributo

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        # print("passou pelo init")
        self.preco = preco

    def desconto(self, percentual):
        # print(type(percentual))
        # print(type(self.preco))
        self.preco = self.preco - (self.preco * (percentual / 100))

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()

    # criando um Getter > pra obter um valor
    @property
    def preco(self):
        return self._preco

    # criando um Setter > vai configurar o meu valor
    # Coloco o nome da propriedade que eu quero, e o setter depois, como no exemplo
    @preco.setter
    def preco(self, valor):
        # print('chamou o preço')
        # estou verificando se o valor que foi passado é uma instancia de string(str)
        if isinstance(valor, str):
            # converto para float e uso um replace para retirar o cifrao (R$)/poderiaa usar expressoes regulares
            valor = int(valor.replace('R$', ''))

        self._preco = valor


# quando eu chamo minha classe, com os parametros eu preencho meus atributos
produto1 = Produto('CAMISETA', 50)
produto1.desconto(10)
print(produto1.nome, produto1.preco)

# passando valor de uma maneira ('R$15) incorreta paraser corrigitos no meu getters e setters
produto2 = Produto('CANECA', 'R$15')
produto2.desconto(10)
print(produto2.nome, produto2.preco)
