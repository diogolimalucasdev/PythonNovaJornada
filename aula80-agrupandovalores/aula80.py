from itertools import groupby, tee

alunos = [
        {'nome': 'Diogo Lima' , 'nota': 'A'} ,
        {'nome': 'Leticia' , 'nota': 'B'} ,
        {'nome': 'Roberto' , 'nota': 'C'} ,
        {'nome': 'Joao' , 'nota': 'D'} ,
        {'nome': 'Eduardo' , 'nota': 'D'} ,
        {'nome': 'Andre' , 'nota': 'B'} ,
        {'nome': 'Anderson' , 'nota': 'B'} ,
        {'nome': 'Jose' , 'nota': 'A'} ,
        {'nome': 'Fabricio' , 'nota': 'C'}
]

# ordenar a lista por nota

alunos.sort(key=lambda item: item['nota']) #preciso ordenar os dados para usar a função groupby

# for aluno in alunos:
#     print(aluno)

alunos_agrupados = groupby(alunos, lambda item:item['nota']) #agrupe os alunos pela chave nota

for agrupamento, valores_agrupado  in alunos_agrupados: #agrupamento é a chave e valores agrupados os valores
    va1, va2 = tee(valores_agrupado) #faço uma copia do meu interador para duas variaveis
    print(f"\n agrupamento: {agrupamento}")

    for aluno in va1:
        print(f"\t{aluno}")

    quantidade = len(list(va2))
    print(f"\t{quantidade} alunos tiraram a nota {agrupamento}")


