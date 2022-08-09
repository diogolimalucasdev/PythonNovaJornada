"""
fazer com que o programa execute varias coisas ao mesmo tempo,
normalmente nosso codigo é executado de maneira linear
"""

from time import sleep
from threading import Thread, Lock

"criando thread - 1 maneira"
# class Meuthread(Thread):
#     def __init__(self, texto, tempo):
#         self.texto = texto
#         self.tempo = tempo
#
#         "chamandar o init da propria thread"
#         super().__init__()
#
#     def run(self):
#         sleep(self.tempo)
#         print(self.texto)
#
# """minha thread 1 vai demorar 5 segundos
# essa thread vai ser executado independete do que esta acontencendo na minha main thread
# assim minha thread1 vai executar ao mesmo tempo que meu for que esta seguindo a logica linear
# """
# t1 = Meuthread('Thread 1', 5)
# t1.start()
#
# """
# Eu posso criar quantos threads eu quiser e ao mesmo tempo tambem
# """
# t2 = Meuthread('Thread2 executou ', 10)
# t2.start()
#
# t3 = Meuthread('thread3 executou', 10)
# t3.start()
#
# for i in range(20):
#     print(i)
#     sleep(1)

"thread 2 maneira"
#
#
# def vai_demorar(texto, tempo):
#     sleep(tempo)
#     print(texto)
#
#
# t1 = Thread(target=vai_demorar, args=('olá mundo 1', 1))
# t1.start()
#
# t2 = Thread(target=vai_demorar, args=('olá mundo 2', 4))
# t2.start()
#
#
# t3 = Thread(target=vai_demorar, args=('olá mundo 3', 5))
# t3.start()
#
# "executando na minha thread principal"
# for i in range(20):
#     print(i)
#     sleep(.5)


"utlizando de outra maneira"

# def vai_demorar(texto, tempo):
#     sleep(tempo)
#     print(texto)
#
#
# t1 = Thread(target=vai_demorar, args=('olá mundo 1', 10))
# t1.start()
#
# #eu tofroçando meu codigo principal esperar a thread acabar
# "enquanto minha t1 estiver viva is_alive() =viva o funcionando eu fico esperando minha thread acabar"
# while t1.is_alive():
#     print('Esperando a thread.')
#     sleep(2)
#
# print('A thread acabou')

"fazendo com a que thread se junto com a principal, nao faz muito sentido mas tem como"
# def vai_demorar(texto, tempo):
#     sleep(tempo)
#     print(texto)
#
#
# t1 = Thread(target=vai_demorar, args=('olá mundo 1', 10))
# t1.start()
# # para que isso aconteça eu utilizo o join
# t1.join()
# print('Thread acabou')

"risco que pode acontecer com a thread quando estamos fazendo maninupalçao de dados"


class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        "o lock serve para trancar dentro do meu metodo"
        self.lock = Lock()

    def comprar(self, quantidade):
        "tranco o metodo por dentro do metodo"
        self.lock.acquire()
        if self.estoque < quantidade:
            print('Não temos ingressos suficientes.')
            self.lock.release()
            return

        sleep(1)
        self.estoque -= quantidade
        print(f'Voce comrpou {quantidade} ingresso(s). Ainda temos {self.estoque} em estoque')

        'quando ele terminar tudo eu libero o metodo, com isso eu nao permito que exista varios entrando dentro' \
        'do meu metodo e executando de maneira desorganizada e quebrando o codigo e a condição if'
        self.lock.release()


if __name__ == '__main__':
    ingressos = Ingressos(10)

    threads = []
    for i in range(1, 20):
        "utilizando o thread para comprar ingressos, pois podemos ter varios compradores simultaneos"
        t = Thread(target=ingressos.comprar, args=(i,))
        threads.append(t)

    "pecorra minha lista de threads e start cada uma"
    for t in threads:
        t.start()

    executando = True
    while executando:
        "logo de cara ja jogo minha variavel executando para false pois vou fazer a validação logo abaixo!"
        executando = False

        "pecorra minha lista de threads novamente "
        for t in threads:
            "minha threads esta viva? se estiver mude o estado da variavel executando para True"
            if t.is_alive():
                executando = True
                break

        "quando acabar e minha variavel executando for False, printa pra mim o valor da variavel estoque"
    print(ingressos.estoque)

