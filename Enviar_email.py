# Uma funcao para meche com o servico smtp, com o intuito de reutilizar codigo e melhorar a identacao
import email.message as email_message
import smtplib
import codigos_adicionais.users_secretos as codigo

def Send_mails(email : str,corpo_email : str, titulo : str):
    try:
        smtp_conection = Conectar_smtp()
        smtp_conection.sendmail("verificar254@gmail.com",email,Montando_html_email(email,corpo_email,titulo).as_string()) 
        smtp_conection.quit()
    except Exception as erro:
        with open("log-de-erro","a") as arquivo:
            arquivo.write("\n")
            arquivo.write(f"{erro}")

def Conectar_smtp():
    coneccao = smtplib.SMTP("smtp.gmail.com",587,timeout=8)
    coneccao.starttls()
    coneccao.login("verificar254@gmail.com",codigo.codigo)
    return coneccao


def Montando_html_email(email_add : str, corpo :str, titulo : str):
    corpo_email = email_message.Message()
    corpo_email["from"] = "BitJoin verificar254@gmail.com"
    corpo_email['to'] = email_add
    corpo_email['subject'] = titulo
    corpo_email.add_header("Content-Type","text/html")
    corpo_email.set_payload(corpo,"utf-8")
    return corpo_email