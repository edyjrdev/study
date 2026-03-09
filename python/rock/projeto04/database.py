from flask_sqlalchemy import SQLAlchemy  # BD
"""
flask shell
db.create_all() - Cria banco \instance\database.db
Ver com Extensão SQLIte Viewer no VS Code
db.session
db.session_commit() - Salva no DB
"""

db = SQLAlchemy()  # Criar conexão
# Session -> conexão ativa
