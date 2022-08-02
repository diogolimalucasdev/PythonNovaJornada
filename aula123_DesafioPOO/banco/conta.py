from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self.saldo = saldo

    @property
    def agencia(self):
        return self._agencia


    def saldo(self):
        return self.saldo

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Valor do depositor precisa ser numérico!")

        self.saldo += valor
        print("Deposito realizado com sucesso! ")

    @abstractmethod
    def sacar(self):
        pass
