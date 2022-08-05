from string import Template
from datetime import datetime

with open('../aula141_Enviandoemails/template.html', 'r', encoding="utf-8") as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='Diogo',data=data_atual)

print(corpo_msg)