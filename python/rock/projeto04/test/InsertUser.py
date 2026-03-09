import os
import sys

# When running this file directly, ensure the project root is on sys.path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from app import app
from model.user import User
from database import db
import bcrypt

def cria_user_admin():
    password='admin123'
    with app.app_context():
        senha_hash = bcrypt.hashpw(str.encode(password), bcrypt.gensalt())
        if not User.query.filter_by(username='admin').first():
            user = User(username='admin', password=senha_hash, role='admin')
            db.session.add(user)
            db.session.commit()
            print('Usuário admin criado.')
        else:
            print('Usuário admin já existe.')


if __name__ == '__main__':
    cria_user_admin()
