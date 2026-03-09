# Teste Unitario
import pytest
import requests

BASE_URL='http://127.0.0.1:5001'
tasks = []  # lista de tarefas


# pystest testa funções iniciadas com test_

# CRUD
# Create
def test_create_task():
    #body
    task_test = {
        "title": "Tarefa de Teste",
        "description": "Descrição da Tarefa de Teste."
    }

    response = requests.post(f'{BASE_URL}/tasks', json=task_test)
    assert response.status_code == 200
    json_response = response.json()
    assert "message" in json_response
    assert "id" in json_response
    tasks.append(json_response['id'])

# Read
# List
def test_list_tasks():
    response = requests.get(f'{BASE_URL}/tasks')
    json_response = response.json()
    assert response.status_code == 200
    assert "tasks" in json_response
    assert "total_tasks" in json_response

# Task by id
def test_get_task_by_id():
    #ler lista de tarefas de teste
    if tasks:
        task_id = tasks[0]  # pegar primeira task
        response = requests.get(f'{BASE_URL}/tasks/{task_id}')
        json_response = response.json()
        assert response.status_code == 200
        assert task_id == json_response['id']
 
# Update
def test_update_task():
    #ler lista de tarefas de teste
    if tasks:
        task_id = tasks[0]  # pegar primeira task
        payload = {
            "description": "Teste Update Task",
            "done": True,
            "title": "Teste Update Task"
        }
        response = requests.put(f'{BASE_URL}/tasks/{task_id}', json=payload)
        json_response = response.json() 
        assert response.status_code == 200
        assert "Teste Update Task" in json_response['title']
        # comparar todos campos
        response = requests.get(f'{BASE_URL}/tasks/{task_id}')
        json_response = response.json()
        assert payload['title'] == json_response['title']
        assert payload['done'] == json_response['done']
        assert payload['description'] == json_response['description']

# Delete
def test_delete_task():
    if tasks:
        task_id = tasks[0]
        response = requests.delete(f'{BASE_URL}/tasks/{task_id}')
        assert response.status_code == 200

        response = requests.get(f'{BASE_URL}/tasks/{task_id}')
        assert response.status_code == 404