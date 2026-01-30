# funcoes

def saudacao(nome, sexo):
    match sexo.upper():
        case 'M':
            print(f'Bem vindo, {nome}')
        case 'F':
            print(f'Bem vinda, {nome}')
        case _:
            print(f'Olá, {nome}')
    

nome_usuario= input('Qual seu nome?')
sexo_usuario = input("Qual seu sexo?' ('M', 'F' ou 'NI')")

saudacao(nome_usuario, sexo_usuario)      

def quadrado(numero):
    return numero ** 2

print(quadrado(12))
print(quadrado(113))

def soma(num1, num2):
    resultado = num1 + num2
    return resultado

n1 = 10
n2 = 55
print(f'Soma {n1} e {n2} é {soma(10, 51)}')