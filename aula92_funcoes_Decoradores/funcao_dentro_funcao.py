def master():
    def slave():
        print('oi')

    slave()


master()  # eu chamo a master e a master executa a função escrava, pois esta dentro do corpo da funcao master


# possa fazer assim tambem
def principal():
    def secundaria():
        print('oi secundaria')

    return secundaria


variavel = principal()
variavel()


# possa fazer dessa outra mandeira tambem
def master(funcao):
    def slave():
        funcao()

    # quando eu nao coloco os parentes significa que ue to retornando sem executar a função (na variavel eu executo)
    # ja se eu coloco os parentes eu estou retornando ela exceutada (na variavel eu nao executo)
    # prestar atenção nisso, pois muda o jeito de chamar ela depois
    return slave


def fala_oi():
    print("oi funções")


fala_oi = master(fala_oi) #estou decorando a fução, pois a fala oi ficou escrava da master
fala_oi()

print("\nUsando o decorador:")
#fazendo de uma maneira mais comum de se ver
def master_suprema(funcao):
    def slave_suprema():
        print("Estou decorada")
        funcao()

    return slave_suprema

#usando o decorador
@master_suprema
def fala_ola():
    print('ola')

fala_ola()
