# comparações
# == - igual
# != - diferente
# > - maior
# < - menor
# >= - maior ou igual
# <= -menor ou igual
# and - E lógico
# or - OU lógico
# not - Negado

# if elfis e else

resposta = input('Quantos anos você tem?')

idade = int(resposta)

bebe = idade >=0 and idade <= 3
crianca = idade > 3 and idade <= 12
adolescente = idade > 12 and idade <= 17
adulto = idade > 18 and idade <= 65
idoso = idade > 65 and idade <= 100
lenda = idade > 100 and idade <= 150

if bebe:
    print('Bebê')
elif crianca:
    print('Criança')
elif adolescente:
    print('Adolescente')
elif adulto:
    print('Adulto')
elif idoso:
    print('Idoso')
elif lenda:
    print('Lenda')
else:
    print('Alien')

a = None

# match x:
#   case value:

match a:
    case 1:
        print(a)
    case 2:
        print(a)
    case _:
        print(a)