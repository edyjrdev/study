print('Exemplo de uso de modulo padrão:')

import math as m  # Matematica - importa tudo do modulo

n_usr = input('Digite um numero para calculo da raiz quadrada:')
try:
    numero = float(n_usr)
    raiz = m.sqrt(numero)
except Exception as e:
    print(f'Erro: {e}')
else:
    print(f'Raiz quadrada de {numero} é {raiz}')

from math import pi  # importação especifica de parte

n_usr = input('Digite um raio de circulo para calculo do diametro:')
try:
    numero = float(n_usr)
    diametro = 2 * pi * numero  # pi da math 
except Exception as e:
    print(f'Erro: {e}')
else:
    print(f'Raio de{numero} produz cículo de diametro {diametro}')

print('Uso de Modulo personalizado')

import meu_modulo as mymod

mymod.saudacao('Edy')
mymod.saudacao('Laila', 'F')

numero = 10
resultado = mymod.dobro(numero)
print(f'O quadrado de {numero} é {resultado}')

