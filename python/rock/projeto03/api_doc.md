# API Rest

## Metodos HTTP

### GET (Consulta Recurso)
Estado atual do recurso (endpoint).

### POST (Inserir Recurso)
Inserir informações em um recurso.
Informações no Body.

### PUT (Atualizar Tudo no Recurso)
Atualizar todas as informações em um recurso. Sobreescreve todas informações.

### PATCH (Atualizar Parcial do Recurso)
Atualizar parcialmente as informações em um recurso.

### DELETE (Remover Recurso)
Remover o recurso.

## Código de Response Http
### 100 - 199 - Informativo
### 200 - 299 - Sucesso
200 - Sucesso
201 - Criação de Recuros
### 300 - 399 - Redirecionamento
### 400 - 499 - Erro do Cliente
400 - Erro de Requisição (Bad Request)
401 - Não Autorizado
403 - Proibido (acesso não autorizado)
404 - Recurso Não Encontrado
405 - Método Não Permitido
### 500 - 599 - Erro do Servidor
500 - Erro Interno do Servidor
501 - Não Implementado
502 - Bad Gateway
503 - Serviço Indisponível
504 - Gateway Timeout
505 - Versão do Protocolo Não Suportada

## Swagger
https://editor.swagger.io/

