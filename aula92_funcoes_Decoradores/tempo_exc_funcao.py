from time import time
from time import sleep

def velcodiade(funcao):
    def interna(*args, **kwargs):
        start_time = time() #hora atual
        resultado = funcao(*args, **kwargs)
        end_time = time() #hora atual em que finalizou a função
        tempo_exc = (end_time - start_time) * 1000 #quero em milesegundos
        print(f"\n A função {funcao.__name__} levou {tempo_exc:.2f}ms para executar")
        return resultado
    return interna

@velcodiade
def demora():
    for i in range(10):
        # print(i)
        print(i, end = '')
        sleep(1) # a cada volta do for ee dorme por um segundo, ao todoo é 5 segundos

demora()