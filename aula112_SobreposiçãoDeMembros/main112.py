from classes112 import *

cliente1 = ClienteVIP('diogo', 21, 'Lima')

"quando eu chamo o falar, o python primeiro procura primeiro na classe ClienteVIP se ele nao encontrar" \
"ele vai subindo as cadeias, vai procurar em Cliente se existe algum metodo com esse nome, se ele nao encontrar" \
"ele vai ate Pessoa e vai porcurar esse metodo"
cliente1.falar()
