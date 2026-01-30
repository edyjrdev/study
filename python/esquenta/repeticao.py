# linha
def linha():
    print('-' * 25)


# for
for i in range(1, 11):
    print(i)

familia = ['Edy', 'Laila', 'Sara', 'Luca', 'Hani', 'Zig', 'Rafik', 'Peka', 'Greta']

for parte in familia:
    print(parte)
linha()


tupla = ('F', 'M', "NI")
for sexo in tupla:
    print(sexo)
linha()

dicionario = {
    'nome': 'Edy Junior'
    , 'idade':  48
    , 'sexo': 'M'
    , 'email': 'edyjrdev@gmail.com'
    , 'cidade': 'Brasília'
    , 'uf': 'DF'
}

for chave, valor in dicionario.items():
    print(f'{chave}:{valor}')
linha()

for chave in dicionario.keys():
    print(chave)
linha()

for valor in dicionario.values():
    print(valor)    
linha()

# pegando indice da lista com len() e range()
lista_uf = ['ac', 'al', 'ap', 'am', 'ba', 'ce', 'df', 'es', 'go', 'ma', 'mt', 'ms', 'mg', 'pa', 'pb', 'pr', 'pe', 'pi', 'rj', 'rn', 'rs', 'ro', 'rr']
for i in range(0, len(lista_uf)):
    print(i, lista_uf[i].upper())
linha()

# enumerate retorar indice e valor.
for indice, valor in enumerate(lista_uf):
    print(indice, valor.upper())
linha()


# while
# equanto condicao:
#    processa
#   altera condicao

contador = 1
voltas = 10
while contador < voltas:
    print(contador)
    contador += 1
linha() 

permanecer = True
execucoes = 0
while permanecer:
    execucoes += 1
    resposta = input(f'{execucoes} Deseja permanecer? (S) ou (N)')
    if resposta.upper() == 'S':
        permanecer = True
    elif resposta.upper() == 'N':
        print('Adeus')
        permanecer = False
linha()

max_tentativa = 3
tentativa = 0
senha = '1234'                  
while tentativa < max_tentativa:
    resposta = input('Digite sua senha:')

    if resposta == senha:
        print('Autorizado')
        break
    else:   
        tentativa += 1
        if max_tentativa == tentativa:
            print('Bloqueado')
        else:
            print(f'Senha incorreta. Mais {max_tentativa - tentativa}')