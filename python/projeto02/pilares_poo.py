# Herança em POO


class Animal:
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def emitir_som(self):
        pass

    def andar(self):
        print(f'O {self.nome} andou.')


# Subclasse - Classe Filha
class Cachorro(Animal):
    def __init__(self, nome: str) -> None:
        super().__init__(nome)  # Inicializa Pai

    # Polimorfismo no metodo
    def emitir_som(self):
        return 'Au, au, au'

class Gato(Animal):
    def __init__(self, nome: str) -> None:
        super().__init__(nome)  # Inicializa Pai

    # Polimorfismo no metodo    
    def emitir_som(self):
        return 'Miau, miau'


dog = Cachorro('Zig')
cat = Gato('Felix')

animais = [dog, cat]

for animal in animais:
    print(f'{animal.nome} soa com {animal.emitir_som()}')  # Metodo sobrescrito do pai
    print(f'{animal.nome} andou.')  # Metodo Herdado

# Encapsulamento (atributos privados)

class ContaBancaria:
    def __init__(self, saldo) -> None:
        self.__saldo = saldo  # __ mostra que deve ser privado
    
    # Proteção do Saldo Privado
    def get_saldo(self):  
        return self.__saldo


    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
    
    def sacar(self, valor):
        if self.__saldo >= valor and valor > 0:
            self.__saldo -= valor

cc = ContaBancaria(500)
print(f'Saldo inicial: {cc.get_saldo()}')
cc.depositar(1)
cc.depositar(-1)
cc.sacar(252)
print(f'Saldo Final: {cc.get_saldo()}')

# Abstração (Não permite instancia) - Classe Abstrata - Vira Obrigação de Implementação

from abc import ABC, abstractmethod

# ABC - Molde de Classe Abstrata

class Veiculo(ABC):
    
    @abstractmethod  # decorador para tornar metodo abstrato
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass


class CarroErrado(Veiculo):
    def __init__(self):
        pass
try:
    camaro = CarroErrado() # Erro de Instanciacao
except Exception as e:
    print(e)
"""
TypeError: Can't instantiate abstract class Carro without an implementation for abstract methods 'desligar', 'ligar'
"""

class Carro(Veiculo):
    def __init__(self, modelo='Fusca') -> None:
        self.__modelo = modelo

    
    def get_modelo(self):
        return self.__modelo

    def ligar(self):
        return f'{self.get_modelo()} ligado'
    
    def desligar(self):
        return f'{self.get_modelo()} desligado'

uno = Carro('Uno')
print(uno.ligar())
print(uno.desligar())

fusca = Carro()
print(fusca.ligar())
print(fusca.desligar())
