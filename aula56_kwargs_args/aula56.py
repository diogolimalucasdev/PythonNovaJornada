"""
funções (def) em python - *args **kwargs
"""


# apartir que eu crio um padrao(nome=None) todos meus proximos argumentos tem que ter um padrao

# def func(a1, a2, a3, a4, a5, nome=None, a6): #moddo errado, o a6 esta incorreto

# modo certo
def func(a1 , a2 , a3 , a4 , a5 , nome = None , a6 = None):
    print(a1 , a2 , a3 , a4 , a5 , nome , a6)
    return nome , a6


var = func(1 , 2 , 3 , 4 , 5 , nome = 'Diogo' , a6 = '5')
print(var)

lista = [1 , 2 , 3 , 4 , 5]
n1 , n2 , *n = lista  # n1 = 1 n2 = 2 *n=[3,4,5]

# desempacotado minha lista
lista2 = [1 , 2 , 3 , 4 , 5 , 6]
print(*lista2 , sep = "")


################# ARGS ###########################################
# agora se eu nao sei quantos argumentos irao vim pra minha função, neste caso eu uso o *args
# parecido com a lista, lembrando que desse jeito o args vem como uma tupla, por isso transformo em list
def func2(*args):
    args = list(args)
    print(args)
    print(args[0])
    args[0] = 20

    print(len(args))


func(1 , 2 , 3 , 4 , 5 , 6 , 7)

#outro exemplo de args
def func3(*args):
    print(args)

lista_func3 = [4 , 5 , 6 , 7 , 8 , 9]
func3(*lista_func3)  # envio minha lista descompactada, para que nao se torne uma tupla dentro de uma tupla


######################## KWARGS #######################################

#kwargs sao argumentos nomeados, como por exemplo

def func5(*args, **kwargs):
    print(args) #aqui nesse print os kwargs nao irao aparecer, pois eles estao nos kwargs
    print(kwargs) #aqui vai aparecer meu nome e sobrenome, aqui ira aparecer dentro de chaves
    print(kwargs['nome'], kwargs['sobrenome']) #aqui eu acesso ao meu argumento nome que no caso é diogo e o sobrenome

    #se eu quiser saber se alguem mandou o argumento nome eu faço assim
    nome = kwargs.get('nome')
    print(nome)

    #tentando pegar um kwargs que nao foi passado para ver o que ele me retorna
    idade = kwargs.get('idadde')

    if idade is not None:
        print(idade)
    else:
        print('Idade nao existe')

list_func5 = [2,3,5,6,7,8]
func5(*list_func5, nome='Diogo', sobrenome='Lima') #aqui eu to passando um argumento nomeado, nome='Diogo'
