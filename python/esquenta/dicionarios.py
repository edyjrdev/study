# dicionarios - chave:valor, não ordenado

dicionario = {
    'nome': 'Edy Junior'
    , 'idade': 48
    , 'sexo': 'M'
    , 'email': 'edyjrdev@gmail.com'
    , 'cidade': 'Brasilia'
}

dicionario_numero = {
    1: 836
    , 2: 491
    , 3: 661
}

print(dicionario)
print(dicionario['nome'])
print(dicionario['idade'])

print(dicionario_numero)
print(dicionario_numero[2])

# adicionar chave
dicionario['estado'] = 'DF'
print(dicionario)
dicionario_numero[4] = 999
print(dicionario_numero)

#atualizar
dicionario_numero[4] = 55
print(dicionario_numero)

#del - para remover
del dicionario_numero[1]
print(dicionario_numero)

# metodos
# keys
chaves = dicionario.keys() 
print(list(chaves))

# values
valores = dicionario.values()
print(list(valores))

# items - retorna tupla -> chave, valor
items = dicionario.items()
tuplas = list(items)
print(tuplas)
print(tuplas[0][0])  # chave
print(tuplas[0][1])  # valor