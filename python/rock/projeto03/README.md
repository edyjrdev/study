# Projeto03 - Tasks API

Documentação e instruções rápidas para executar a API e acessar a especificação OpenAPI/Swagger.

## Instalação

Instale dependências (recomenda-se um virtualenv):

```bash
pip install -r requirements.txt
```

## Rodar a aplicação

```bash
python app.py
```

A aplicação roda por padrão em `http://localhost:5001`.

## Endpoints de documentação

- Swagger UI (Flasgger): http://localhost:5001/apidocs
- Spec JSON: http://localhost:5001/swagger.json
- Spec YAML: http://localhost:5001/swagger.yaml

## Endpoints da API

- `POST /tasks` — criar tarefa
- `GET /tasks` — listar tarefas
- `GET /tasks/{id}` — pegar tarefa por id
- `PUT /tasks/{id}` — atualizar tarefa
- `DELETE /tasks/{id}` — remover tarefa

## Observações

- `swagger.yaml` e `swagger.json` foram gerados estaticamente a partir das docstrings.
- Se preferir que a UI aponte para `/swagger.yaml`, edite a inicialização do Flasgger no `app.py`.
