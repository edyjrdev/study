import time
import os


# tarefa = dicionario com nome e status
tempo_espera = 2
tarefas = []
ico_aberta = '🆕'
ico_fechada = '✔️'
status_dom = [{'A': 'Aberta'}, {'C': 'Completa'}]

def get_ico_tarefa(tarefa):
    return ico_aberta if tarefa['status'] == 'Aberta' else ico_fechada

def indice_valido(tarefas, indice):
    return indice >= 0 and indice < len(tarefas)

def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa = {'nome': nome_tarefa, 'status': 'Aberta'}
    tarefas.append(tarefa)
    print(f'Tarefa "{nome_tarefa}" adicionada com sucesso!')
    print(f'Total de tarefas: {len(tarefas)}')
    
def ver_tarefas(tarefas):
    print('Lista de tarefas:')
    if len(tarefas) > 0 :
        for i, tarefa in enumerate(tarefas, start=1):
            ico_tarefa = get_ico_tarefa(tarefa)
            print(f'{i}.[ {ico_tarefa} ] {tarefa["nome"]}')
    else:
        print('Nenhuma tarefa encontrada')
    
def atualizar_tarefa(tarefas):    
    ver_tarefas(tarefas)
    num_tarefa = input('Digite a numero da tarefa para atualizar:')
    idx_tarefa = int(num_tarefa) - 1
    if indice_valido(tarefas, idx_tarefa):
        tarefa = tarefas[idx_tarefa]
        novo_nome = input('Digite o novo nome da tarefa: ')
        tarefa['nome'] = novo_nome
        novo_status = input('Digite o novo status da tarefa: (A) = Aberta, (C) = Completa: ')

        match novo_status.upper():
            case 'A':
                novo_status = 'Aberta'
            case 'C':
                novo_status = 'Completa'
            case _:
                print(f'{novo_status} Status inválido. Salva como Aberta')
                novo_status = 'Aberta'

        tarefa['status'] = novo_status
        ico_tarefa = get_ico_tarefa(tarefa)
        print(f'[ {ico_tarefa} ] Tarefa "{tarefa["nome"]}" atualizada com sucesso !') 
    else:
        print(f'{num_tarefa} inválido para lista')

    
def completar_tarefa(tarefas):
    ver_tarefas(tarefas)
    num_tarefa = input('Digite a numero da tarefa para completar:')
    idx_tarefa = int(num_tarefa) - 1
    if indice_valido(tarefas, idx_tarefa):
        tarefa = tarefas[idx_tarefa]
        tarefa['status'] = 'Completa'
        ico_tarefa = get_ico_tarefa(tarefa)
        print(f'[ {ico_tarefa} ] Tarefa "{tarefa["nome"]}" completa com sucesso !')
    else:
        print(f'{num_tarefa} inválido para lista')

def deletar_completas(tarefas):
    ver_tarefas(tarefas)
    print('Deletar completas')
    for i, tarefa in enumerate(tarefas, start=1):
        if tarefa['status'] == 'Completa':
            del tarefas[i-1]
            print(f'Tarefa "{tarefa["nome"]}" deletada com sucesso!')       
    print(f'Total de tarefas: {len(tarefas)}')

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
            nome_tarefa = input('Digite o nome da tarefa: ')
            adicionar_tarefa(tarefas, nome_tarefa=nome_tarefa)
       
        case '2':
            ver_tarefas(tarefas)
        case '3':
            print('Atualizar tarefa')
            atualizar_tarefa(tarefas)
        case '4':
            print('Completar tarefa')
            completar_tarefa(tarefas)
        case '5':
            print('Deletar completas')
            deletar_completas(tarefas)  
        case '6':
            print('Adeus')
            break
        case _:
            print('Opção inválida')
    time.sleep(tempo_espera)
    os.system('cls')