
import datetime
import flask_limiter 
import threading
from flask import Blueprint,request
import flask_limiter.util
from Database.database import Usuarios
import email.message as email
import smtplib
from codigos_adicionais.users_secretos import codigo
app = Blueprint("Salvando email",__name__)


# Salva o email na db  e verifica 
@app.route("/",methods=["POST"])
def Salvando_email_db():
    nome = request.form.get("nome")
    email = request.form.get("email")
# faz a verificacao dos valores e retorna se e valido 
    resultado_da_verificacao = verificando_valores(nome,email)
    if Usuarios.select().where((Usuarios.email == email)).exists():
        return 'O email ja esta cadastrado',403
    if resultado_da_verificacao:
        with threading.Lock(): # trava a execucao duplicada do codigo 
            threading.Thread(target=Enviar_pra_db,args=(nome,email)).start()
            return 'Sucesso',200
    elif resultado_da_verificacao is None:
        return 'O Email inserido e invalido',403
    elif not resultado_da_verificacao:
        return 'O nome inserido e invalido',403
    

#verifica os valores passados 
def verificando_valores(nome : str, email : str): 
    if not isinstance(nome,str) or not isinstance(email,str):
        return False
    if len(nome) < 2 or len(nome) > 30:
        return False # false e erro de nome invalido
    if len(email) > 30 or len(email) < 4  :
        return None #  none e erro de email invalido
    if ({'%','*','/','(','#','`'}.intersection(nome + email)):
        return False
    if not '@' in email or not ".com" in email:
        return None
    if not email.split(".")[1] == 'com':
        return None
    return True


#envia os dados para a db 
def Enviar_pra_db(nome : str, email : str):
    Usuarios.create(nome=nome,email=email,inserido_data=datetime.datetime.now().date())
    Funcao_principal(email,nome)

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
    corpo_email['subject'] = "Seja bem vindo "
    corpo_email.add_header("Content-Type","text/html")
    corpo_email.set_payload(body_email,"utf-8")
    return corpo_email


# envia e salva o codigo html 
def enviar_email_boas_vindas(addres : str, nome : str, coneccao_smtp : smtplib.SMTP):

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
            display: inline-block();
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
            <h1>Bem vindo ao nosso sistema de cadastro</h1>
        </div>
        <div class="content">
            <p>Olá {nome}</p>
            <p>Olá! Nos da equipe BitJoin estamos muito feliz por tê-lo(a) em nosso grupo de atualizações. Enviaremos o resumo do valor do Bitcoin diariamente às 6:25 (horário de Brasília).</p>
            <p>Seja bem-vindo(a) à comunidade BitJoin!</p>

            <p>Acompanhe as cotacoes de moedas em tempo real em nosso site</p>
            <p><a href="https://www.youtube.com" class="cta-button">Confira a Cotação Atual</a></p>
        </div>
        <div class="footer">
            <p>Você está recebendo este e-mail porque se inscreveu em nosso site para receber atualizações sobre o Bitcoin.</p>
            <p><a href="https://www.youtube.com/unsubscribe">Cancelar inscrição</a></p>
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
            enviar_email_boas_vindas(email,nome,conecao_smtp)
            conecao_smtp.quit()

