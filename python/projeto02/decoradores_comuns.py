# decorradores comuns
# @classmethod
# @staticmethod

class MinhaClasse:
    vida = 10 # atributo da classe

    def __init__(self, nome):
        self.nome = nome

    def metodo_de_instancia(self):
        return f'Método da instância chamado por {self.nome} de vida {self.vida}'
    
    @classmethod
    def metodo_da_classe(cls):
        return f'Método da classe chamado para vida {cls.vida}'  # acesa atributo da classe, mas não da instancia (nome)
    
    @staticmethod
    def metodo_estatico():
        return 'Método estatico sem acesso a atributo de classe e atributo da instancia'
    

obj = MinhaClasse('Herói')
print(obj.metodo_de_instancia())
try:
    print(MinhaClasse.metodo_de_instancia())  # tentando chamar metodo sem passar instancia (self)
except Exception as e:
    print(e)
"""
TypeError: MinhaClasse.metodo_de_instancia() missing 1 required positional argument: 'self'
"""
print(obj.vida)
print(MinhaClasse.metodo_da_classe()) # Sem ter criado instancia
print(MinhaClasse.metodo_estatico())

# uso @classmethod para instanciar classe (antes do construtor)


class Carro:
    def __init__(self, marca: str, modelo: str, ano: int):
        self.marca = marca.upper()
        self.modelo = modelo.upper()
        self.ano = ano
    
    @classmethod
    def criar_carro(cls, configuracao_csv):
        marca, modelo, ano = configuracao_csv.split(',')  # desempacota para o construtor
        return cls(marca, modelo, int(ano))  #chamada do construtor
    
    def show(self):
        return f'Modelo:{self.modelo}\nMarca:{self.marca}\nAno Fabricação:{self.ano}'
    
    
config_polo = 'Volks,Polo,2013'
config_uno = 'Fiat,Uno,1988'

polo = Carro.criar_carro(config_polo)
print(polo.show())
uno = Carro.criar_carro(config_uno)
print(uno.show())