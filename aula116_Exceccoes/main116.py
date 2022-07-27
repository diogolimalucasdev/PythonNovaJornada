"""
Excecções personalizadas
"""

"""
se depois de pesquisar todos os erros padroes do python eu nao encontrei um que representa o 
erro em questao eu posso criar um tratamento personalizado

"""

class TaErradoError(Exception):
    pass

def testar():
    raise TaErradoError('Errado!')

try:
    testar()
except TaErradoError as error:
    print(f'Erro: {error}')