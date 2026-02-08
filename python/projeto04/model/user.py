from database import db  # db = instancia do SQLAlchemy
from flask_login import UserMixin  # metodos de autenticação

class User(db.Model, UserMixin):  # Herança Multipla tudo do SQLAlchemy e UserMixin
    # id,(int), username (text), password (text) - v1
    # id,(int), username (text), password (text), role (text) - v2
    # Mapeamento de colunas
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)  # Unico não aceita nulo
    password = db.Column(db.String(80), nullable=False) # não aceita nulo
    role = db.Column(db.String(10), nullable=False, default='user')  # dominio: admin, user
"""
Criar usuario admin
flask shell
user = User(username='batman', password='batcave123')
db.session.add(user)
db.session.commit()

# reinicializar db
db.drop_all()
db.session.commit()
exit()

# recriar db
db.create_all()
db.session.commit()

"""
