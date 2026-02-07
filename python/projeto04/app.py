from flask import Flask, request, jsonify
from database import db
from model.user import User
from flask_login import LoginManager, login_user, current_user, logout_user, login_required


app = Flask(__name__)
# Secrety Key e Conexão BD
app.config['SECRET_KEY'] = 'chave_secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin123@127.0.0.1:3306/flask-crud'

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
                        "message":f"Bem vindo, {user_db.username.upper()} como {user_db.role.upper()}.",
                        "username": user_db.username
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

# Usuarios
# Create User
@app.route('/user', methods=['POST'])
@login_required  # Somente Usuario Existente
def create_user():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username and password:
        #cadastrar
        user = User(username=username, password=password, role='user')  # adicionar usuario com role menor
        
        # Possivel erro de integridade (unique username)
        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            print(e)
            return jsonify({"message": "Erro de criação"}), 500    
        return jsonify({
            "message": f"Usuário {user.username.upper()} cadastrado com {user.role.upper()} com sucesso."}), 200
    else:
        return jsonify({
            "message": "Dados inválidos.",
            "campos": {"username": username, 
                       "password": password} 
        }), 401  # Requisição inválida

# Get User
@app.route('/user/<int:id>', methods=['GET'])
@login_required
def get_user_by_id(id):
    user_db = User.query.get(id)

    if user_db:
        return jsonify({"username": user_db.username})
    return jsonify({"message":"Usuário não cadastrado."}), 404

@app.route('/user/<int:id>', methods=['PUT'])
@login_required
def update_user_by_id(id):
    data = request.json
    nova_senha = data.get('password')
    user_db = User.query.get(id)
    cur_user = User.query.get(current_user.id)
    # usario com role admin pode alterar qualquer usuario
    # usuario com role user nao pode alterar outro usuario
    outro_usuario = id != current_user.id
    role_user = current_user.role == 'user'

    if outro_usuario and role_user:
        return jsonify({"message": f"Operaçao nao permitida para {cur_user.role.upper()}."}), 403  # Proibido

    if user_db and nova_senha :
        user_db.password = nova_senha # ja faz no bd
        db.session.commit()

        return jsonify({"message": f"{user_db.username.upper()} atualizado."})
    return jsonify({"message":"Usuário não cadastrado."}), 404

# Delete usuario
# Get User
@app.route('/user/<int:id>', methods=['DELETE'])
@login_required
def delete_user_by_id(id):
    cur_user = User.query.get(current_user.id)

    eh_user_logado = id == cur_user.id
    
    role_user = current_user.role == 'user'
    # User nao passara
    if role_user:
        return jsonify({"message": f"Operaçao nao permitida para {cur_user.role.upper()}."}), 403  # Proibido 
    
    # Nao pode apagar o usario logado
    if eh_user_logado:
        return jsonify({"message":f"Ação não permitida, não é possivel deletar usuário logado:{cur_user.username.upper()}.", 
                "id": id}), 403 # Não permitido

    user_db = User.query.get(id)
    if user_db:
        username_del = user_db.username
        db.session.delete(user_db)
        db.session.commit()
        return jsonify({"message": f"{username_del} deletado."})
    return jsonify({"message":"Usuário não cadastrado."}), 404

if __name__ == '__main__':
    # DEV com debug On
    # BASE_URL = http://127.0.0.1:5001
    app.run(debug=True, port='5001')