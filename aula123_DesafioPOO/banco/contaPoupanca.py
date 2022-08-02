from aula123_DesafioPOO.banco.conta import Conta


class ContaPoupanca(Conta):
    def __init__(self, agencia, conta, saldo):
        super().__init__(agencia, conta, saldo)

    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente')
            return


        self.saldo -= valor
        print(f'Saque realizado, Agencia: {self.agencia}, Conta: {self.agencia} '
              f'saldo: {self.saldo}')
