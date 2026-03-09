# decoradores - tags que alteram comportamento embrulhando uma função

def meu_decorador(func):  # recebe a função como objeto
    # embrulha a função com comportamento
    def wrapper():
        print('Antes da função ser chamada no decorador.')  # executa antes da função
        func()
        print('Depois da função ser chamada no decorador.')  # executa depois da função
    return wrapper

@meu_decorador
def minha_funcao():
    print('Minha função executando.')

minha_funcao()

# exemplo @usuario_logado -> funcionalidade

print('-' * 30)
# Decorador Como Classe
class MeuDecoradorDeClasse:
    def __init__(self, func):  # função que sera embrulhada
        self.func = func
    
    def __call__(self):
        print('Antes da função ser chamada (decorador de classe)')
        self.func()
        print('Depois da função ser executada (decorador de classe)')

@MeuDecoradorDeClasse
def minha_funcao_com_classe():
    print('Minha função embrulhada com Decorador de Classe.')

minha_funcao_com_classe()