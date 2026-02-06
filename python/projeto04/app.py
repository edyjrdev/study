from flask import Flask, request, jsonify
from database import db
from model.user import User
from flask_login import LoginManager, login_user, current_user, logout_user, login_required


app = Flask(__name__)
# Secrety Key e Conexão BD
app.config['SECRET_KEY'] = 'chave_secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# passar configurações do app para o database
login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)

#view login
login_manager.login_view = 'login'

# carregar usuário - na sessão
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    
    username = data.get('username')
    password = data.get('password')
    if username and password:
        # login

        # consultar username no br
        user_db = User.query.filter_by(username=username).first()  # Pega o primeiro registra da lista da consulta
        # usuario existe
        if user_db:
            # se exister conferir senha
            if user_db.password == password:
                login_user(user_db)  # Header da response com Set-Cookie -> session=<HASH>
                print(current_user.is_authenticated)
                return jsonify(
                    {
                        "message":f"Bem vindo, {username.upper()}.",
                        "username": username
                    }
                ), 200  # Sucess (Padrão)
        else:
            # sem user or password
            return jsonify(
            {
                "message":f"Usuário {username} é inválido."
            }
        ), 400  # Forbiden

    else:
        # sem user or password
        return jsonify(
            {
                "message":"Credenciais inválidas."
            }
        ), 400  # Forbiden

@app.route('/logout', methods=['GET'])
@login_required  # decorator que projege rotada - Erro: 405
def logout():
    logout_user()  # Limpar Cookie - session
    return jsonify({"message":"Logout realizado com sucesso."})


@app.route('/')  # endpoint
def root():
    return "Flask Ok."

"""
@app.route("/hello-word", methods=['GET'])
def hello_world():
    return "Hello Word."
"""

if __name__ == '__main__':
    # DEV com debug On
    # BASE_URL = http://127.0.0.1:5001
    app.run(debug=True, port='5001')