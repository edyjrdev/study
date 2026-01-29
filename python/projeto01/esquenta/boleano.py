# bool 
True # Verdadeiro
False # Falso

# Condicionais
idade = 120
menor_idade = idade < 18 and idade >=0
maior_idade = idade >= 18 and idade < 65
melhor_idade = idade >=65 and idade < 80
anciao = idade >= 80 and idade < 100
lenda = idade >= 100 and idade <=150

if menor_idade:
    print('Menor de idade')
elif maior_idade:
    print('Maior de idade')
elif melhor_idade:
    print('Melhor idade')
elif anciao:
    print('Ancião')
elif lenda:
    print('Lenda')
else:
    print('Alien')