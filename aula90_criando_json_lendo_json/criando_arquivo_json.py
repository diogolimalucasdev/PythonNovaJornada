import json

d1 = {
        'Pessoa 1': {
                'nome': 'Diogo' ,
                'idade': 21
        } ,
        'Pessoa 2': {
                'nome': 'Maria' ,
                'idade': 44
        } ,
}

d1_json = json.dumps(d1 , indent = True)  # transformando meu dicionario para json

# jogando isso em um arquivo json

with open('arquivo.json' , 'w+') as file:
    file.write(d1_json)
