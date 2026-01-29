# Comentário de uma linha

# Forçar erro de sintaxe.
# SyntaxError: invalid syntax

"""
Docstring for python.projeto01.sintaxe
Comentário de Multiplas linhas ou string com quebra de linha
"""

# Quebrando string sem """
nome_completo = 'Edy ' + \
'Epumuceno Rodrigues ' + \
'Junior'

print(nome_completo)

idade = 48
maior_idade = idade >= 18

# sequencia serial
if maior_idade:
    #bloco verdadeiro
    print('Maior de idade')
    print(idade)
else:
    # bloco falso
    print('Menor de idade')

print('Você nasceu em:' + str(2026 - idade))