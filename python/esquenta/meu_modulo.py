def saudacao(nome, sexo='M'):
    match sexo.upper():
        case 'M':
            print(f'Bem vindo, {nome}')
        case 'F':
            print(f'Bem vinda, {nome}')
        case _:
            print(f'Olá, {nome}')


def dobro(numero):
    return numero * 2