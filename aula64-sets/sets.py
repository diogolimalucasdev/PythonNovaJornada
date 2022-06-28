#parecido com lista e dicionario, mas nao podemos acessar index do meu set

#add(adiciona), update(atualiza), clear, diascar
#union | (une)
#intersection & (todos os elemetos presentes nos dois sets)
#difference - (elemetos apenaqs no set da esquerda)
#symmetric_difference ^(elementos que estão nos dois sets, mas nao em ambos)

s1 = {1,2,3,4,5}
print(type(s1))
s1.discard(2)
print(s1)

s1.update(['Python']) #sempre mandar em lista no set pois ele nao segue ordem
s1.update([6,7,8,9,10])
print(s1)

#podemos remover valores duplicados de uma lista dessa maneira
lista = [1,2,3,4,5,'DIOGO', 'DIOGO'] #observe que o nome esta duplicado
lista = set(lista) #transformei para set
print(lista) #agora tudo que estava duplicado sumiu
lista = list(lista) #e transformo para lista novamente, tem que tomqar cuidado com os elementos fora de ordem
print(lista)



l1 = {1,2,3,4,5,7}
l2 = {1,2,3,4,5,6}

l3 = l1 | l2  #union
print(l3)

l3 = l1 & l2  #intersection
print(l3)

l3 = l1 - l2 #diferrence sempre priorizando o primeiro set
print(l3)

l3 = l2 - l1 #diferrence sempre priorizando o primeiro set
print(l3)



l3 = l1 ^ l2 #elementos que estao em cada um mas nao em ambos
print(l3)
