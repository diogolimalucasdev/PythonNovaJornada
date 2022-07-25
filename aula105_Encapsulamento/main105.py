"""
public: sao metodos e atribudos que podem ser acessados dentro e fora da classe
protected: sao atributos que podem ser caessados dentro daquela classe ou das filhas daquela classse
private: so esta disponivel dentro da classe
"""
"""
Em python utilizamos:
protected(é publico) _ 1 underline  e quando eu faço isso quando eu vou na minha instancia da minha classe tento acessar 
meu atributo ele nao aparece "privato mais fraco"
privado __ 2 underline "privato mais forte"



"""


class BaseDeDados:
    "contructor"

    def __init__(self):
        self.__dados = {}

    "crio um getter para que apenas seja apenas visualizado mmeu atributo"
    @property
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_cliente(1, 'Diogo')
bd.inserir_cliente(2, 'Miguel')
bd.inserir_cliente(3, 'Maria')
bd.apaga_cliente(2)

"veja como fica quando eu tento acessar um privado  e o codigo nao quebra"
# bd.__dados = "uma outra coisa"

"se eu for printa agora o bd.__dados ele vai me dar uma resposta asssim: 'uma outra coisa' "
# print(bd.__dados)

"se eu quiser acessar meu atributo privado, eu faço asssim "
# print(bd._BaseDeDados__dados)


"agora se fosse apenas um underline o codigo seria quebrado pois é apenas um protected"
"lembrando que pra testar isso tenho que colocar apenas um underline no meu atributo"
# bd._dados = 'uma outra coisa'

# bd.lista_clientes()

"posso tambem criar um getter onde ue permito que apenas seja acessado o valor desse meu atributo"
"assim eu consigo acessar meu atributo mas nao consigo modifica-lo"
print(bd.dados)

'se eu fizer isso vai dar uma excecção'
bd.dados = "uma outra coisa"