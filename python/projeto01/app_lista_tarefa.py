import time
import os


while True:
    menu = ['1. Adicionar tarefa'
        , '2. Ver tarefas'
        , '3. Atualizar tarefa'
        , '4. Completar tarefa'
        , '5. Deletar completas'
        , '6. Sair']
    
    print('APP de Lista de Tarefas')
    for menu in menu:
        print(menu)

    escolha = input('Escolha uma opção válida : ')
    match escolha:
        case '1':
            print('Adicionar tarefa')   
        case '2':
            print('Ver tarefas')
        case '3':
            print('Atualizar tarefa')
        case '4':
            print('Completar tarefa')
        case '5':
            print('Deletar completas')  
        case '6':
            print('Adeus')
            break
        case _:
            print('Opção inválida')
    time.sleep(1)
    os.system('cls')