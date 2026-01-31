# aplicação flask
from flask import Flask

app = Flask(__name__)  # nome do arquivo atual __main__

# rota para comunicar com usuario
@app.route('/')  # endpoint
def hello_word():
    return "Hello Word Flask."

@app.route('/about')
def about():
    return 'Sobre o Flask'

@app.route('/autor')
def autor():
    return '<p>Edy Epumuceno Rodrigues Junior<br>edyjrdev@gmail.com</p>'

# DEV - rodando local
# porta padrão 5000
"""Foi feita uma tentativa de acesso a um soquete de uma maneira que é proibida pelas permissões de acesso"""
# trocar porta para 5001
if __name__ == '__main__':
    app.run(debug=True, port=5001)  # inicializa aplicação em modo debug