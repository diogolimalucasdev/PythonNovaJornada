#https://docs.python.org/3.0/library/datetime.html
from datetime import datetime, timedelta

#timedelta = intervalo de tempo

data = datetime(2022, 8, 2, 17, 54) #ano, mes, dia, hora, minuto
print(data) #padrao americano, geralmente salvamos assim em uma base de dados

"para colocar no padrao em que eu desejo eu faço o seguinte"
print(data.strftime('%d/%m/%Y %H:%M:%S')) #dia, mes,ano com 4 digitos, hora, minuto e segundo


"recebendo data em formado de string"

data_string = datetime.strptime('20/04/2022', '%d/%m/%Y') #primeiro é a data em string e o segundo o formato
print(data_string)

"convertendo timestamp em data timestamp é o segundos"

data_timestamp = datetime.fromtimestamp(1555729200.0)
print(data)


"adicionando dias a uma data"

data_adicionada = datetime.strptime('02/08/2001 20:00:00', '%d/%m/%Y %H:%M:%S' )
data_adicionada = data_adicionada + timedelta(days=5)
print(data_adicionada.strftime('%d/%m/%Y %H:%M:%S'))


"comparando dois dias "

data_inicial = datetime.strptime('20/04/1990 20:00:00', '%d/%m/%Y %H:%M:%S')
data_final = datetime.strptime('25/04/1990 22:33:00', '%d/%m/%Y %H:%M:%S')

diferenca = data_final - data_inicial
print(diferenca)

"ver so a hora"
print(data_inicial.time())

"ver so os dias de diferença"
print(diferenca.days)

"ver a diferença de segundos de uma hora pra a outra"
print(diferenca.total_seconds())