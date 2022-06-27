clientes = {
        'cliente1': {
                'nome': 'Diogo' ,
                'sobremome': 'Lima' ,
                'cargo': 'programador Python'
        } ,
        'cliente2': {
                'nome': 'João' ,
                'sobremome': 'Moreira' ,
                'cargo': 'programsdor Js' ,
        } ,
}

# intrerando no dicionario

# primeiro for responsavel pelo lop completo do dicionario

"""
Cliente k é chave do dicionario composto, cliente_v é os dados nome e sobrenome
"""
for clientes_k , cliente_v in clientes.items():
    print(f'Exibindo {clientes_k}')

    # o segundo for eu to pecorrendo o dicionario de cada cliente
    """
    dados K éa chave(nome e sobrenome) e o dados v é o valor de cada chave(diogo, lima; joao moreira)
    """
    for dados_k , dados_v in cliente_v.items():
        # \t serve para dar um tab no print
        print(f'\t{dados_k} = {dados_v}')
