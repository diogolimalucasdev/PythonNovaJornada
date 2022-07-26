"""
Super Classe
"""

"""
As setinhas mostra aonde esta sendo utilizando e aonde esta sendo sobescrito
"""
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print('falando')
        print(f'{self.nomeclasse} que chamou e esta falando')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} comprando ')

    """
    antes eu tinha testado deixando na minha classe Super Pessoa, mas trouxe o metodo para cliente
    para ver como o python trablharia, depois se quiser fazer o teste é so comentar esse metodo abaixo
    """
    def falar(self):
        print("Estou em cliente agora")


class ClienteVIP(Cliente):
    """
    eu posso sobrepor meu constructotr de Pessoa desse jeito:
    posso adicionar atributos ao meu constructor ja que estou sobescrevendo ele
    """
    def __init__(self, nome, idade, sobrenome):
        """
        Eu chamo o meu constructor da minha classe Pessoa e sobescrevo ele adicionando o
        atributo sobrenome
        """
        Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome


    """
    posso sobescrever metodos dentro da minha classe como por exemplo
    esse metodo tava em pessoa e eu sobescrevendo ele"""
    def falar(self):
        """eu posso executar um metodo da minha classe super antes de executar na minha filha
            utilizando o super().o nome do metodo que eu quero chamar

            O python vai buscar o primeiro metodo nas classe acima, e a primeira que ele encontrar ele
            vai parar
        """
        super().falar()
        """
        ja se eu quero especificar de um onde eu quero meu metodo eu utlizo assim:
        sembre lembrando que neste caso eu tenho que passar minhas instancia (self)
        """
        Pessoa.falar(self)
        """
        como eu fiz com a classe Pessoa eu tambem posso realizar com a cliente
        """
        Cliente.falar(self)
        print("Sobreposição de metodo")

        print("utilizando o contructor dessa classe....\n")
        print(f'{self.nome}, {self.sobrenome}')


