"""
A herança vem de cima pra baixo

Animal -> respirar
    Lobo(Animal) -> respirar / uivar
    Cachorro(Lobo) -> respirar / uivar / latir
"""

"""
nesse  momento eu to tentando pegar um metodo da minha classe filha para a classe pai
isso nao é muito comum mas é apenas para entender 
Biblioteca -> chama_interface
    Interface(Biblioteca) -> metodo da interface
        metodo_da_interface
"""

from classes.interface import Interface

interface1 = Interface()
interface1.chama_metodo_da_interface()