"""
Em pythohn tudo é objeto: incluindo classes, metaclasses sao as "classes" que ciram classes.
type é uma metaclasse(!?)
"""

"""
criando metaclasse
"""
class Meta(type):
    """
    com esse metodo eu verifico quando novas classes sao criadas e passo alguns argumentods
    mcs = meta classe, name= noma da classe criada, bases = as classes pais que serao criadas
    namespace = toda classe tem seu namspace
    """

    def __new__(mcs, name, bases, namespace):
        """
        nao quero que minha classe A se comporte como as outras
        """
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)

        if 'b_fala' not in namespace:
            print(f'Oi, voce precisa criar o metodo b_fala em {name} ')
        else:
            "aqui eu verifico novamente se esse b_fala é um metodo mesmo"
            if not callable(namespace['b_fala']):
                print(f'b_fala precisa ser um método, nao atributo em {name}')

        return type.__new__(mcs, name, bases, namespace)


"""
com esse argumento metaclass = Meta eu falo como que eu quero minha classe se comporte por meio da Meta
"""
class A(metaclass=Meta):
    def fala(self):
        self.b_fala()


class B(A):
    # teste = 'Valor'
    # b_fala = 'trolei'
    def b_fala(self):
        print('oi')

    def seil_la(self):
        pass


# b = B()
# b.fala()
