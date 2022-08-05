from string import Template
from datetime import datetime
from dados_email import meu_email, minha_senha

from email.mime.multipart import MIMEMultipart #assunto da msg e pra quem ta sendo enviado a msg
from email.mime.text import MIMEText  #texto da msg
from email.mime.image import MIMEImage #a imagem para ser anexado
import smtplib #conectar ao servidor do gmail

with open('template.html', 'r', encoding="utf-8") as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='Diogo',data=data_atual)

msg = MIMEMultipart()
msg ['from'] = 'Diogo Lima Lucas' #quem esta enviando
msg['to']= meu_email #para quem
msg['subject'] = 'Atenção esse é um email de teste' #assunto

"enviando o html para msg"
corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

with open('imagem.jpg', 'rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img)


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        "msg de hello para o servidor"
        smtp.ehlo()
        smtp.starttls()
        "email que esta enviando a msg"
        smtp.login(meu_email, minha_senha)
        smtp.send_message(msg)
        print('E-mail enviado com sucesso')
    except Exception as e:
        print('Email nao enviado!')
        print('Erro: ', e)
