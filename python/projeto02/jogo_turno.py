# Jogo em Turno de Heroi contra Vilao

import os, time

@staticmethod
def linha():
    print('-' * 30)

@staticmethod
def linha_especial():
    print('*' * 30)


class Personagem:
    def __init__(self, nome: str, vida: int, nivel_dano: int):
        self.__nome = nome
        self.__vida = vida
        self.__nivel_dano = nivel_dano

    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida
    
    def get_nivel_dano(self):
        return self.__nivel_dano
    
    def show(self):
        return f'Nome:{self.get_nome()}\nVida:{self.get_vida()}\nNível:{self.get_nivel_dano()}'

    def atacar(self, alvo):
        dano = self.get_nivel_dano() * 2
        alvo.receber_ataque(dano)
        linha_especial()
        print(f'{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano.')
        linha_especial()

    def receber_ataque(self, dano):
        self.__vida -= dano
        morreu = self.__vida < 0
        if morreu:
            self.__vida = 0

class Heroi(Personagem):
    def __init__(self, nome, vida, nivel_dano, super_poder):
        super().__init__(nome, vida, nivel_dano)
        self.__super_poder = super_poder
    
    def get_superpoder(self):
        return self.__super_poder
    
    def show(self):
        return f'{super().show()}\nSuper Poder:{self.get_superpoder()}'
    
    def especial(self, alvo):
        dano = self.get_nivel_dano() * 5
        alvo.receber_ataque(dano)
        linha_especial()
        print(f'{self.get_nome()} usou {self.get_superpoder()} e causou {dano} de dano no {alvo.get_nome()}.')
        linha_especial()

class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel_dano, tipo):
        super().__init__(nome, vida, nivel_dano)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo

    def show(self):
        return f'{super().show()}\nTipo:{self.get_tipo()}'
    

class JogoTurno:
    """
    Classe orquestradora do Jogo de Turno Heroi vs Vilão
    """
    
    def __init__(self):
        self.heroi = Heroi('Salvador', 110, 5,'Super Força')
        self.vilao = Inimigo('Ciclope', 85, 2, 'Místico') 

    def inicializar_batalha(self):
        print('Inicio da Batalha')
        heroi_vivo = self.heroi.get_vida() > 0
        vilao_vivo = self.vilao.get_vida() > 0 
        turnos = 0
        while heroi_vivo and vilao_vivo:
           turnos += 1
           linha()
           print(f'Turno: {turnos}')
           print('Situação Personagems')
           linha()
           print(self.heroi.show())
           linha()
           print(self.vilao.show())
           
           input('Pressione Enter para atacar...')
           escolha = input('Escolha (1) = Ataque normal, (2) = Especial: ')
        
           match escolha:
               case '1':
                   self.heroi.atacar(self.vilao)
                   time.sleep(3)
               case '2':
                   self.heroi.especial(self.vilao)
                   time.sleep(3)
               case _:
                   print('Opção inválida.')

           #vez do vilao
           vilao_vivo = self.vilao.get_vida() > 0
           if vilao_vivo:
               self.vilao.atacar(self.heroi)
               time.sleep(3) 
           heroi_vivo = self.heroi.get_vida() > 0

           if heroi_vivo and not vilao_vivo:
               print(f'Parabéns, {self.heroi.get_nome()} ganhou com {self.heroi.get_vida()} de vida')
               time.sleep(2) 
           elif not heroi_vivo and vilao_vivo:
               print(f'Que pena, você perdeu do {self.vilao.get_nome()} ganhou com {self.vilao.get_vida()} de vida') 
               time.sleep(1) 
               
           os.system('cls')

jogo = JogoTurno()
jogo.inicializar_batalha()
linha_especial()
print('Fim de Jogo.')