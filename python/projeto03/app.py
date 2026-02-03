# aplicação flask
from flask import Flask, request, jsonify

#modelo
from models.task import Task

app = Flask(__name__)  # nome do arquivo atual __main__

# exemplo
"""

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
"""
    

# CRUD
# Create, Read, Update, Delete
# SQL = Insert, Select, Update, Delete
# Tabela: Tarefa (task)

tasks = [] # lista de tarefas em memoria.
task_id_control = 1

#Create Task
@app.route('/tasks', methods=['POST'])
def create_task():
    #Receber informações do Cliente
    global task_id_control  # Dar acesso a variavel local
    data = request.get_json()  # Pega Json do body da requisição
    # Requisicao do Flask
    print('body:',data)

    new_task = Task(id=task_id_control
                 , title=data['title']
                 , description=data.get("description","")
                 , done=data.get("done",False))  # Se não enviou insere vazia
    tasks.append(new_task)
    task_id_control += 1

    print(len(tasks))

    return jsonify(
        {"message": f"Tarefa {new_task.id} criada com sucesso"}
        )

# Create Read
@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]
    
    output = {
                "tasks": task_list,
                "total_tasks": len(task_list)
            }
    return jsonify(output)

# Select by task_id
@app.route('/tasks/<int:id>', methods=['GET'])
def get_task_by_id(id):
    for task in tasks:
        if task.id == id:
            return jsonify(task.to_dict())
            break
    if not task:
        return jsonify({"message": f"Tarefa {id} não encontrada"}), 404  # Código de retorno não encontrado.


# Update by task_id -> body para dados
@app.route('/tasks/<int:id>', methods=['PUT'])
def set_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break
    if task == None:
        return jsonify({"message": f"Tarefa {id} não encontrada"}), 404
    
    data = request.get_json()
    #campos atualizaveis
    task.title = data['title']
    task.description = data.get("description","")
    task.done = data.get("done",False)

    return jsonify({"message":f"Tarefa {id} atualizada com sucesso"})

# Delete
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    for t in tasks:
        if t.id == id:
            tasks.remove(t)
            return jsonify({"message":f"Tarefa {id} removida com sucesso"})
            break       
        
    return jsonify({"message":f"Tarefa {id} não encontrada"}), 404





# Teste de Parametro na URL (str)
"""
@app.route('/user/<username>', methods=['GET'])
def show_user(username):
    print(username, type(username))
    return f'Usuário: {username}'

# Teste de Parametro na URL (str -> int) - Conversão do Flask
@app.route('/user/<int:cpf>', methods=['GET'])
def show_cpf(cpf):
    print(cpf, type(cpf))
    return f'CPF: {str(cpf)}'

# Teste de Parametro na URL (str -> int) - Conversão do Flask
@app.route('/user/<float:salario>', methods=['GET'])
def show_salario(salario):
    print(salario, type(salario))
    return f'Salário: {salario:.2f}'
"""




# DEV - rodando local
# porta padrão 5000
"""Foi feita uma tentativa de acesso a um soquete de uma maneira que é proibida pelas permissões de acesso"""
# trocar porta para 5001
if __name__ == '__main__':
    app.run(debug=True, port=5001)  # inicializa aplicação em modo debugim