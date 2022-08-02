from pessoa import Pessoa
from banco.cliente import Cliente
from banco.contaCorrente import ContaCorrente
from banco.contaPoupanca import ContaPoupanca
from banco.banco import Banco
from banco.conta import Conta

banco = Banco()

pessoa1 = Pessoa('diogo', 21)
cliente1 = Cliente(pessoa1.nome, pessoa1.idade)
conta1 = ContaCorrente(1111, 2222, 0)
cliente1.inserir_conta(conta1)
banco.inserir_cliente(cliente1)
banco.inserir_conta(conta1)

if banco.autenticar(cliente1):
    cliente1.conta.sacar(20)
else:
    print("cliente nao autenticado")

pessoa2 = Pessoa('maria', 22)
cliente2 = Cliente(pessoa2.nome, pessoa2.idade)
conta2 = ContaPoupanca(2222, 3333, 0)
cliente2.inserir_conta(conta2)
banco.inserir_cliente(cliente2)
banco.inserir_conta(conta2)

if banco.autenticar(cliente2):
    cliente2.conta.depositar(20)
    cliente2.conta.sacar(10)
else:
    print("cliente nao autenticado")






