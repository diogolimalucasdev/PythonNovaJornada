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

        "e aqui eu faço o if para que ele nao seja sobescrito e utilizo o del para apagar toda vez que ele for escrito"
        if 'attr_classe' in namespace:
            print(f'{name} Tentou sobescrever o atributo')
            del namespace['attr_classe']

        return type.__new__(mcs, name, bases, namespace)


"""
Agora eu vou fazer de uma forma para que meu atributo nao seja sobescrito
"""
class A(metaclass=Meta):
    attr_classe = 'Valor A'


class B(A):
    attr_classe = 'Valor B'


b = B()
print(b.attr_classe)
