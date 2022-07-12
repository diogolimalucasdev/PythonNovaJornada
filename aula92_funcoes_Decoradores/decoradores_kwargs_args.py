def master(funcao):
    def slave(*args, **kwargs):
        print('agora eu estou decorada')
        funcao(*args, **kwargs)
    return slave

@master
def outra_funcao(msg):
    print(msg)


outra_funcao("Ola eu sou o Diogo")
