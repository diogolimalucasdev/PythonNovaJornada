"""
combinations, permutations e product - Itertools
Combinação - Ordem nao importa
Permutação - Ordem importa
Ambos nao repetem valores unicos
Produto - Ordem importa e repete valores unicos
"""
from itertools import combinations, permutations, product

pessoas =['Diogo', 'Laryssa', 'Maria', 'Miguel', 'Fidelcino', 'Nilton']


#como ver quantas combinações ao possiveis, onde a ordem nao importa - combinations
print("\n Com combinations \n")
for grupo in combinations(pessoas, 2): #passo a lista e informo de quanto em quanto é a combinações
    print(grupo)



#como ver quantos combinações são possiveis onde a ordem importa - permutations
print("\n Com permutation \n")
for grupo in permutations(pessoas, 2):
    print(grupo)

#como ver quantas combinações ao possiveis, onde a ordem importa e os valores se repetem nas combinações - product

print("\n Com product \n")
for grupo in product(pessoas, repeat=2):
    print(grupo)