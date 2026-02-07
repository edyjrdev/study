import os
import sys

# When running this file directly, ensure the project root is on sys.path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from app import app
from model.user import User
from database import db

def cria_user_admin():
    with app.app_context():
        if not User.query.filter_by(username='admin').first():
            user = User(username='admin', password='admin123', role='admin')
            db.session.add(user)
            db.session.commit()
            print('Usuário admin criado.')
        else:
            print('Usuário admin já existe.')


if __name__ == '__main__':
    cria_user_admin()
