from app import *
from db import adicionar_contato, selecionar_usuarios

@app.route("/")
def index():
    return render_template("home.html")

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/quemsomos')
def quemsomos():
    return render_template('quemsomos.html')


@app.route('/contato', methods=["POST", "GET"])
def contato():
    if request.method == "POST":
        email = request.form["email"]
        assunto = request.form["assunto"]
        descricao = request.form["descricao"]

        adicionar_contato(email=email, assunto=assunto, descricao=descricao)

        return "Cadastrado com sucesso!<br><a href="/contato">Clique aqui para retornar</a><br><a href="users">Clique aqui para ver os usuários cadastrados</a>"
    return render_template('contato.html')

@app.route("/users")
def users():
    userDetails = selecionar_usuarios()
    return render_template("users.html", userDetails=userDetails)
