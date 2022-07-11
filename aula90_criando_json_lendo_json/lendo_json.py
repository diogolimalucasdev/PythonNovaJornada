import json

import criando_arquivo_json

with open('arquivo.json' , 'r') as file:
    d1_json = file.read()

    # transformando de json para dicionario novamente
    d1_json = json.loads(d1_json)

for k, v in d1_json.items():
    print(k)
    for k1, v1 in v.items():
        print(k1, v1)
