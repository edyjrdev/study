from database import db  # db = instancia do SQLAlchemy
from flask_login import UserMixin  # metodos de autenticação

class User(db.Model, UserMixin):  # Herança Multipla tudo do SQLAlchemy e UserMixin
    # id,(int), username (text), password (text)
    # Mapeamento de colunas
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)  # Unico não aceita nulo
    password = db.Column(db.String(25), nullable=False) # não aceita nulo

"""
Criar usuario admin
flask shell
user = User(username='batman', password='batcave123')
db.session.add(user)
db.session.commit()
"""