from aula123_DesafioPOO.banco.conta import Conta


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):
        if  (self.saldo + self._limite) < valor:
            print("Saldo insuficiente")
            return


        self.saldo -= valor
        print(f'Saque realizado, Agencia: {self.agencia}, Conta: {self.agencia}'
              f' saldo: {self.saldo}')
