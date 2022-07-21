from classes import Escritor, Caneta, MaquinaDeEscrever

escritor = Escritor('Diogo')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

print(escritor.nome)
print(caneta.marca)

# fazendo associação das classes
# no momento eu estou enviando para meu atributo ferramenta todo o objeto da classe maquina/caneta
escritor.ferramenta = maquina

# e aqui eu acesso o metodo que esta dentro da maquina mas que eu associei a meu atributo
escritor.ferramenta.escrever()
