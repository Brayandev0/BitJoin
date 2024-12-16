import datetime
import email.message as email
import os
from time import sleep
import threading
from flask import Blueprint
from Database.database import Usuarios
import smtplib
from codigos_adicionais.users_secretos import codigo
from Pagina_principal import dados_request as btc
app = Blueprint("comando",__name__)

def conectando_smtp():
    coneccao = smtplib.SMTP("smtp.gmail.com",587,timeout=8)
    coneccao.starttls()
    coneccao.login("verificar254@gmail.com",codigo)
    return coneccao

def definindo_corpo_email(addres : str,body_email):
    corpo_email = email.Message()
    corpo_email["from"] = "BitJoin verificar254@gmail.com"
    corpo_email['to'] = addres
    corpo_email['subject'] = "Resumo das Moedas"
    corpo_email.add_header("Content-Type","text/html")
    corpo_email.set_payload(body_email,"utf-8")
    return corpo_email



def Enviar_email(addres : str, nome : str, coneccao_smtp : smtplib.SMTP):

    body_email = f''' <!DOCTYPE html>
    
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cotação do Bitcoin</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }}

        .container {{
            width: 100%;
            max-width: 600px;
            margin: 0 auto;
            background-color: #ffffff;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }}

        .header {{
            text-align: center;
            padding: 20px;
            background-color: #f7931a;
            color: #ffffff;
        }}

        .header h1 {{
            margin: 0;
        }}

        .content {{
            text-align: center; /* Centraliza o conteúdo e o botão */
        }}

        .content a {{
            margin: 20px 0;
        }}

        .content p {{
            font-size: 18px;
            color: #333333;
            line-height: 1.6;
        }}

        .cta-button {{
            display: inline-block;
            background-color: #f7931a;
            color: #ffffff;
            text-decoration: none;
            padding: 10px 20px;
            border-radius: 5px;
            font-size: 16px;
            text-align: center;
            margin: 20px auto; /* Centraliza o botão com margem automática */
        }}

        .footer {{
            text-align: center;
            padding: 10px;
            background-color: #f4f4f4;
            font-size: 14px;
            color: #777777;
        }}

    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Resumo do valor do bitcoin Hoje</h1>
        </div>
        <div class="content">
            <p>Olá {nome}</p>
            <p>Este e um breve resumo do valor do bitcoin hoje dia {datetime.datetime.now().date()}, para mais informacoes sobre cotacoes de outras moedas, acesse nosso site clicando abaixo</p>
            <ul>
                <li><strong> A maior Alta de hoje  :</strong> R$ {btc['BTCBRL']["high"]}</li>
                <li><strong> A maior baixa de hoje :</strong> R$ {btc['BTCBRL']['low']}</li>
                <li><strong> Valor de Compra Atual :</strong> R$ {btc['BTCBRL']['bid']}</li>

            </ul>
            <p>Acompanhe as cotacoes em tempo real em nosso site, ultima atualizacao {datetime.datetime.now().hour}:{datetime.datetime.now().minute}</p>
            <p><a href="https://www.youtube.com" class="cta-button">Confira a Cotação Atual</a></p>
        </div>
        <div class="footer">
            <p>Você está recebendo este e-mail porque se inscreveu para receber atualizações sobre o Bitcoin.</p>
            <p><a href="https://www.youtube.com/unsubscribe">Cancelar inscrição</a></p>
        </div>
    </div>
</body>
</html>
'''

    try:
        coneccao_smtp.sendmail("verificar254@gmail.com",addres,definindo_corpo_email(addres,body_email).as_string()) 
        coneccao_smtp.rset()
        print('passou',addres)
    except Exception as e :
        print("erro",e)

def Funcao_principal():
            with conectando_smtp() as SMtp:
                for users in Usuarios.select():
                    if users.email:
                        Enviar_email(users.email,users.nome,SMtp)
                        print(f"enviou  {users.email},{users.nome}")
                        sleep(4)

if datetime.datetime.now().hour == 18 and datetime.datetime.now().minute == 25:
        execucao_assincrona = threading.Thread(target=Funcao_principal)
        execucao_assincrona.start()