from pessoa import Pessoa  # importando a classe Pessoa

# criar um objeto apartir da minha classe
# to usando um "molde" para criar uma 'pessoa'"
# posso passsar os parametros asssim...
p1 = Pessoa('Diogo' , 21)

# passo que ele vai comer e depois peço para ele parar de comer
p1.comer('maça')  # mando que a pessoa esta comendo
p1.parar_comer()  # mando que a pessoa parou de comer

# mando pra parar de comer para cair na minha condição, pois ja mandei ela parar de comer uma vez
# ou seja, ela nao tem como parar de comer se nao esta comendo
p1.parar_comer()
p1.comer('maça')  # e mando novamente que ela esta comendo

# vou mandar ele falar enquanto come para ver o que o codigo vai me retornar
p1.falar('Poo')

# vou pedir pra ele parar de comer para poder falar
p1.parar_comer()
p1.falar('Poo')

# vou pedir para ele parar de falar
p1.parar_falar()

# vou pedir para ele comer e depois falar para cair na minhha condição
p1.comer('macarrao')
p1.falar('Tentar falar comendo macarrao')

# p1.outro_metodo()
# #ou assim
# p2 = Pessoa() # isso é a instancia da minha classe
# p2.nome = 'Miguel'
# p2.idade = 12


# agora verndo a indepedencia de cada pessoa POO

pessoa1 = Pessoa('Diogo Lima' , 21)
pessoa2 = Pessoa('Maria leondia' , 44)

# vejo como as duas pessoas sao indepedentes, cada um pode realizar sua função sem interferir um aou outro
pessoa1.falar('Eu sou o diogo e gosto de Python')
pessoa2.falar('eu sou a mae do Diogo')

pessoa1.parar_falar()
pessoa2.parar_falar()

# agora mando duas funções diferente e os dois irao realizar mesmo assim, normalmente
pessoa1.falar('Ola')
pessoa2.comer('Maça')

# observo que pessoa2 pode comer enquanto pessoa 1 esta falando, mas pessoa1 nao pode ocmer enquanto ela mesma fala
pessoa1.comer('Pera')

# verificando a variavel da classe de duas maneiras
# 1 - maneira
print(pessoa1.ano_atual)
# 2 - maneira
print(Pessoa.ano_atual)


#sabendo o ano de nasicmento da pessoa
print(pessoa1.get_ano_nascimento())
print(pessoa2.get_ano_nascimento())
