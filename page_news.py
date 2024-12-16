import datetime
from flask import Flask,Blueprint, json, render_template
import requests
import json
from codigos_adicionais.users_secretos import KEY_API
app = Blueprint("news",__name__)
btc_news = ""
dolar = ""
dogecoin = ""
solana = ""
moedas = {}
data = 0

@app.route("/")
def PaginaPrincipal():
    global moedas
    if verificar_data():
        return render_template("pagina_noticias.html",
                               bitcoin_titulo = moedas["bitcoin"]["titulo"],
                               bitcoin_descricao = moedas["bitcoin"]["descricao"],
                               bitcoin_publicacao = moedas["bitcoin"]["data_publicacao"],
                               bitcoin_url = moedas["bitcoin"]["url"],

                               # Passa as variaveis do dolar 
                               dolar_titulo = moedas["dolar"]["titulo"],
                               dolar_descricao = moedas["dolar"]["descricao"],
                               dolar_publicacao = moedas["dolar"]["data_publicacao"],
                               dolar_url = moedas["dolar"]["url"],

                               
                               
                               dogecoin_titulo = moedas["dogecoin"]["titulo"],
                               dogecoin_descricao = moedas["dogecoin"]["descricao"],
                               dogecoin_publicacao = moedas["dogecoin"]["data_publicacao"],
                               dogecoin_url = moedas["dogecoin"]["url"],

    

                               solana_titulo = moedas["solana"]["titulo"],
                               solana_descricao = moedas["solana"]["descricao"],
                               solana_publicacao = moedas["solana"]["data_publicacao"],
                               solana_url = moedas["solana"]["url"],
                               )
                      
                               
                               
    return render_template("pagina_noticias.html",
                               bitcoin_titulo = moedas["bitcoin"]["titulo"],
                               bitcoin_descricao = moedas["bitcoin"]["descricao"],
                               bitcoin_publicacao = moedas["bitcoin"]["data_publicacao"],
                               bitcoin_url = moedas["bitcoin"]["url"],

                               # Passa as variaveis do dolar 
                               dolar_titulo = moedas["dolar"]["titulo"],
                               dolar_descricao = moedas["dolar"]["descricao"],
                               dolar_publicacao = moedas["dolar"]["data_publicacao"],
                               dolar_url = moedas["dolar"]["url"],

                               
                               
                               dogecoin_titulo = moedas["dogecoin"]["titulo"],
                               dogecoin_descricao = moedas["dogecoin"]["descricao"],
                               dogecoin_publicacao = moedas["dogecoin"]["data_publicacao"],
                               dogecoin_url = moedas["dogecoin"]["url"],
                               
                               
                               solana_titulo = moedas["solana"]["titulo"],
                               solana_descricao = moedas["solana"]["descricao"],
                               solana_publicacao = moedas["solana"]["data_publicacao"],
                               solana_url = moedas["solana"]["url"],
                               )

    



def verificar_data():
    global data, btc_news, dolar, dogecoin,timeout,solana
    if data > int(datetime.datetime.now().day) or data == 0:
        data = datetime.datetime.now().day
        solicitar_noticias()
        Pegar_json(dolar,"dolar")
        Pegar_json(btc_news,"bitcoin")
        Pegar_json(dogecoin,"dogecoin")
        Pegar_json(solana,"solana")
        return True
    return False



def solicitar_noticias():
    global dolar,btc_news,dogecoin,solana
    dolar = requests.get(f"https://newsdata.io/api/1/news?apikey={KEY_API}&q=Dolar%20OR%20dolar&language=pt").json()
    btc_news = requests.get(f"https://newsdata.io/api/1/news?apikey={KEY_API}&q=bitcoin&language=pt&category=business").json()
    dogecoin = requests.get(f"https://newsdata.io/api/1/news?apikey={KEY_API}&q=doge&language=pt").json()
    solana = requests.get(f"https://newsdata.io/api/1/news?apikey={KEY_API}&q=Solana%20(Sol)&language=pt ").json()
def Pegar_json(tipo: dict, moeda_tipo: str):
    global moedas
    if tipo["results"]:
        articles = tipo["results"]


        # Procurar o primeiro artigo com descrição válida
        article = next((art for art in articles if art.get('description') and "/" not in art.get('description')), None)
        print(article)
        if article:
            descricao = article.get("description")
            if len(descricao) > 150:
                descricao = descricao[:320]  # Limitar a descrição a 150 caracteres

            moedas[f"{moeda_tipo}"] = {
                'titulo': article.get("title"),
                'descricao': descricao,
                'url': article.get("link"),
                'data_publicacao': article.get("pubDate").split("T")[0]
            }
        else:
            print(f"Erro: Nenhuma descrição válida encontrada nos dados da API para {moeda_tipo}.")
    else:
        print(tipo)
        print(f"Erro: A resposta da API para {moeda_tipo} não contém notícias ou está no formato errado.")
