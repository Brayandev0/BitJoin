
import datetime
import os
import random
import sys
import threading
import time
from flask import Blueprint,request

from Database.database import Usuarios
import email.message as email
import smtplib
from codigos_adicionais.users_secretos import codigo
app = Blueprint("codigos",__name__)
codigos = {} # type:ignore

#Pagina EnviarCodigos- envia os codigos por email 
@app.route("/EnviarCodigo",methods=["POST"])
def Eviando_codigo():
    email = request.form.get("email")
    verificacao = verificar_email(email)
    if verificacao is None:
        return "O Email nao esta cadastrado",403
    if not verificacao:
        return "Email Invalido",403
    if verificacao:
        threading.Thread(target=Funcao_principal, args=(email,Usuarios.select().where((Usuarios.email == email)).get().nome)).start()
        return "Sucesso",200


## Verifica se o codigo e valido 
@app.route("/VerificarCodigo",methods=["POST"])
def Verificar_codigo():
    global codigos
    codigo = request.form.get("codigo")
    email = request.form.get("email")
    if Testar_codigo(codigo) and verificar_email(email):
        if codigos.get(f"{email}"):
            if codigos[f"{email}"]["codigo"] == codigo and codigos[f"{email}"]["timeout"] > time.time():
                Remover_da_db(email)
                return "Sucesso",200

            elif codigos[f"{email}"]["timeout"] < time.time():
                codigos.pop(f"{email}")
                return "codigo expirado",403
        return "codigo incorreto",403
    return f"Codigo ou email Invalido",403




# Verifica o codigo 
def Testar_codigo(codigo : str):
    if codigo:
        if len(codigo) != 6:
            return False
        try:
            int(codigo) + 3
            return True
        except ValueError:
            return False
    return False


def Remover_da_db(email : str):
    if Usuarios.select().where((Usuarios.email == email)).exists():
        Usuarios.delete().where((Usuarios.email == email)).execute()


# verifica o email 
def verificar_email(email : str):
    if email:
        if len(email) <= 5:
            return False
        if "@" not in email:
            return False
        if ".com" not in email:
            return False
        if "." not in email:
            return False
        if not Usuarios.select().where((Usuarios.email == email)).exists():
            return None
        return True
    return False

# realiza a conexao do smpt 
def conectando_smtp():
    coneccao = smtplib.SMTP("smtp.gmail.com",587,timeout=8)
    coneccao.starttls()
    coneccao.login("verificar254@gmail.com",codigo)
    return coneccao


# defini o corpo do email 
def definindo_corpo_email(addres : str,body_email):
    corpo_email = email.Message()
    corpo_email["from"] = "BitJoin verificar254@gmail.com"
    corpo_email['to'] = addres
    corpo_email['subject'] = "Confirmação de solicitação"
    corpo_email.add_header("Content-Type","text/html")
    corpo_email.set_payload(body_email,"utf-8")
    return corpo_email


# envia e salva o codigo html 
def Enviar_codigo_email(addres : str, nome : str, coneccao_smtp : smtplib.SMTP):

    body_email = f''' <!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Confirmação de solicitação</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 30px;
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
            <h1>Confirmação de solicitação</h1>
        </div>
        <div class="content">
            <p>Olá {nome}</p>
            <p>Seu código de verificação Valido por 30 minutos é <strong>{gerar_codigo(addres)}</strong>.</p>

            <p>Se não foi você quem solicitou este código, ignore este e-mail. Para continuar a solicitação, clique no botão abaixo:</p>
            <p><a href="https://www.youtube.com" class="cta-button">Desinscrever</a></p>
            <p><strong>Atenciosamente, Equipe BitJoin</strong></p>
        </div>
        <div class="footer">
            <p>Você está recebendo este e-mail porque solicitou a desinscrição do seu e-mail no nosso site.</p>
        </div>
    </div>
</body>
</html>

'''

    try:
        coneccao_smtp.sendmail("verificar254@gmail.com",addres,definindo_corpo_email(addres,body_email).as_string()) 

    except Exception as e :
        print("erro",e)



## realiza o envio do email de boas vindas 
def Funcao_principal(email : str,nome : str):
        with threading.Lock(): # trava a execucao dupla do codigo 
            conecao_smtp = conectando_smtp()
            Enviar_codigo_email(addres=email,nome=nome,coneccao_smtp=conecao_smtp)
            conecao_smtp.quit()


##gera e retorna o codigo de 6 digitos 
def gerar_codigo(email : str):
    global codigos
    codigos[f"{email}"] = { "codigo" : ''.join(str(random.randrange(0,9)) for i in range(6)),
                           "timeout" : time.time() + 1800 }
    
    return codigos[f"{email}"]["codigo"]
