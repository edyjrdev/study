# listas

lista_numeros = [1, 2, 5, 7, 9, 10, 13, 17]

lista_heterogenea = ['a', 1, 2.0, True, [1, 2]]

print(lista_numeros)
print(lista_heterogenea)

# Consultando lista
print('lista_numeros[0]', lista_numeros[0])

# fatiamento - slice
print(lista_heterogenea[1:4])  # 1 ao 3
print(lista_numeros[:5]) # 0 ao 4
print(lista_heterogenea[3:]) # 3 ao final
print(lista_heterogenea[-1:]) # ultimo

# alterando
lista_heterogenea[0] = 'b'
print(lista_heterogenea)

# metodos
# append
lista_heterogenea.append('novo')
print(lista_heterogenea)

# index
elemento=13
print(lista_numeros.index(elemento))
print(lista_numeros[lista_numeros.index(elemento)])

#insert (indice, elemento)
lista_heterogenea.insert(0, 'primeiro')
lista_heterogenea.insert(2, 'terceiro')
print(lista_heterogenea)

# pop (indice)
removido = lista_heterogenea.pop(1)
print(removido)
print(lista_heterogenea)

# remove (elemento)
lista_heterogenea.remove('primeiro')
print(lista_heterogenea)    

# sort - ordena somente elemetos ordenaveis
lista_numeros.insert(2,-1)
lista_numeros.insert(4,-10)
lista_numeros.insert(-1,-99)
print(lista_numeros)
lista_numeros.sort() # altera lista sem retorno
print('Lista ordenada: ' + str(lista_numeros))

# reverse
lista_numeros.reverse()
print('Lista invertida: ' + str(lista_numeros))

#