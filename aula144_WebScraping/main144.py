import requests  # para realizar as requisições, vai baixar o html
from bs4 import BeautifulSoup  # para manipular o html dentro do python

url = 'https://pt.stackoverflow.com/questions/tagged/python'
"meu html"
response = requests.get(url)
# print(response.text)

"fazer o analise do html e no segundo eu passo o que eu estou passando que no caso é um html"
html = BeautifulSoup(response.text, 'html.parser')

"agora que eu ja tenho meu objeto que é meu html, agora vou escolher o que eu quero pegar do meu html"
"e faço um for nas classes question-summary"
for pergunta in html.select('.s-post-summary'):
    "seleciono apenas as classes que tem esses nomes "
    titulo = pergunta.select_one('.s-post-summary--content-title')
    tempo = pergunta.select_one(".relativetime")
    votos = pergunta.select_one(".s-post-summary--stats-item-number")

    "e uso o .texto para pegar apenas o texto e nao o html"
    print(tempo.text, titulo.text, votos.text, sep='\t')
