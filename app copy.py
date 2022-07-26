from flask import Flask, render_template
#importar biblioteca de data
from datetime import datetime

app = Flask("hello")

#mock - significa substituto, preenchimento default que pode substituir, uma simulação do banco de dados
posts = [
    {
        "title": "O meu primeiro post",
        "body": "Aqui é o texto",
        "author": "Feulo",
        "created": datetime(2022,7,25)
    },
    {
        "title": "O meu Segundo post",
        "body": "Aqui é o texto",
        "author": "Ale",
        "created": datetime(2022,7,26)
    }
]

@app.route("/")
#Por boas práticas eu chamo de index a funçao
#a página que quero renderizar é index.html e quero passar como dado os posts. Entoa posts recebe posts
def index():
    return render_template("index.html", posts = posts)
#depois tenho que arrumar a página index.html para receber posts

#arranquei a rota do Hello world tbm
#@app.route("/")
#@app.route("/hello")
#def hello():
#    return "Hello Word"

#arranquei a rota do meu contato
#@app.route("/meucontato")
#def meuContato():
#    return render_template("index.html", email="alesuzuki@gmail.com",nome="Alessandra Suzuki",telefone="(11)99999-9999")

