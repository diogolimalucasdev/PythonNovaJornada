from eletronico import Eletronico
from log import LogMixin

"""
Crio minha class Smartphone e herdo tudo de eletronico
"""


class Smartphone(Eletronico, LogMixin):
    """
    crio meu init apartir do construcrtor de Eletronico e adiciono mais um atributo que é o...
    ... conectado(conectado a internet ou nao)
    """

    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    """
    para conectar verifico se ele esta desligado ou ligado, veirfico tambem se ja ele ja esta conectado ou nao
    """
    def conectar(self):
        if not self._ligado:
            error = f'{self._nome} nao esta ligado'
            print(error)
            self.log_error(error)
            return

        if self._conectado:
            error = f'{self._nome} ja esta conectado'
            print(error)
            self.log_error(error)
            return

        info = f'{self._nome}  esta conectado'
        print(info)
        self.log_info(info)
        self._conectado = True

    def desconectar(self):
        if not self._conectado:
            error = f'{self._nome} Noa esta conectado'
            print(error)
            self.log_error(error)
            return
        info = f'{self._nome} Noa esta desconectado'
        print(info)
        self.log_info(info)
        self._ligado= False
