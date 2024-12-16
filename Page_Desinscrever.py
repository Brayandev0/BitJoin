from flask import Blueprint,render_template

app = Blueprint("/Desincrever",__name__)

@app.route("/")
def Pagina_desinscrever():
    return render_template("pagina_desinscrever.html")
