import sys
import os

print('--- Checklist de Ambiente ---')
print('Ambiente Python Local Ok')

# Mostra a versão detalhada
print(f'Versão do Python: {sys.version}')

# Mostra apenas a tupla de versão (ex: 3, 11, 5)
v = sys.version_info
print(f'Versão Simplificada: {v.major}.{v.minor}.{v.micro}')

# Mostra o caminho do executável que está sendo usado
# (Fundamental para confirmar se é o do pyenv ou do sistema)
print(f'Executável: {sys.executable}')

print('Ambiente Python Local Ok')

