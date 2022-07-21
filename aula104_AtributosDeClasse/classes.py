# relações entre classes com POO

# uma classe associada a outra mas cada umaa pode sobreviver sozinha

class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None

    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta


# minha classe caneta pode estar assosciada ao meu escritor ou nao
class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print('Caneta esta escrevendo...')


class MaquinaDeEscrever:

    def escrever(self):
        print('Maquina esta escrevendo...')
