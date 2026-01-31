class Animal:
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def emitir_som(self):
        pass

    def andar(self):
        print(f'O {self.nome} andou.')


class Mamifero(Animal):
    def __init__(self, nome: str) -> None:
        super().__init__(nome)
    
    def amamentar(self):
        print(f'{self.nome} precisa se amamentar.')
    
class Ave(Animal):
    def __init__(self, nome: str) -> None:
        super().__init__(nome)
        
    def voar(self):
        print(f'{self.nome} tem asas para voar na maioria da vezes.')


class Morcego(Mamifero, Ave):
    def __init__(self, nome: str) -> None:
        super().__init__(nome)
    
    def emitir_som(self):
        # super().emitir_som() - se tivesse implementação e não precisar de polimorfismo
        return 'Morcego emite som ultrasonico que nao conseguimos ouvir.'
    
batman = Morcego(nome='Batman')

print(f'Nome {batman.nome}')
batman.amamentar() # Classe Pai Mamifero
batman.voar() # Classe Ave
print(f'Som do morcego {batman.emitir_som()}') # Polimorfismo da Classe Pai