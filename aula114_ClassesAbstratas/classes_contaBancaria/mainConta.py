from contaPoupanca import ContaPoupanca
from conta import Conta
from contaCorrente import ContaCorrente

"conta poupança, passando agencia, conta e saldo"
# cp = ContaPoupanca(1111, 222, 0)
# cp.depositar(20)
# cp.sacar(10)
# cp.sacar(10)
# cp.sacar(10)

"conta corrente, passando agencia, conta, saldo e limite(opcional)"
"como é conta corrente eu posos passar do valor do meu saldo mas nao do meu valor de limite"
cc = ContaCorrente(agencia=2222, conta=333, saldo=0, limite=500)
cc.depositar(100)
cc.sacar(250)
cc.sacar(500)
cc.depositar(1000)

"eu nao posso estanciar minha classe abstrata"
# conta = Conta(1111, 222, 0)