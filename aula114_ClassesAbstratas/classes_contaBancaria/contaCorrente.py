from conta import Conta


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):
        "como é conta corrente eu somo o valor do saldo com o limite"
        if (self.saldo + self._limite) < valor:
            print("Saldo insuficiente")
            return

        self.saldo -= valor
        self.detalhe()
