from flask import Flask, render_template, request, url_for, jsonify

from flask_mysqldb import MySQL

app = Flask(__name__)

# conexão com o banco de dados
app.config['MYSQL_Host'] = 'localhost' # 127.0.0.1
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'uvtixqn'
app.config['MYSQL_DB'] = 'contato'

mysql = MySQL(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contato", methods=['GET','POST'])
def contato():
    if request.method == "POST":
        email = request.form['email']
        assunto = request.form['assunto']
        descricao = request.form['descricao']
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contato(email, assunto, descricao) VALUES (%s, %s, %s)", (email, assunto, descricao))
       
        mysql.connection.commit()
        
        cur.close()

        return 'Cadastrado com sucesso!<br><a href="/contato">Clique aqui para retornar</a><br><a href="users">Clique aqui para ver os usuários cadastrados</a>'
    return render_template('contato.html')

@app.route("/quemsomos")
def who():
    return render_template("quemsomos.html")

# rota usuários para listar todos os usuário no banco de dados.
@app.route('/users')
def users():
    cur = mysql.connection.cursor()

    users = cur.execute("SELECT * FROM contato")

    if users > 0:
        userDetails = cur.fetchall()

        return render_template("users.html", userDetails=userDetails)
