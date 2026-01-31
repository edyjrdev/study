# Orientação a Objetos em Python

# Classes (Forma) e Objetos (Instâncias)
import datetime as dt


class Pessoa:
    # Construtor com parametros de inicialização - Sem retorno (None)
    def __init__(self, nome: str, data_nacimento='01/01/1900', sexo='M') -> None:  
        self.nome = nome  # atributo da classe
        self.sexo = sexo  # atributo da classe

        # Normalize/parse birthdate: accept 'dd/mm/YYYY' string, datetime.date, or datetime.datetime
        if isinstance(data_nacimento, str):
            try:
                self.data_nacimento = dt.datetime.strptime(data_nacimento, '%d/%m/%Y').date()
            except ValueError:
                # Fallback: try year-only like '1978' -> 01/01/<year>
                try:
                    self.data_nacimento = dt.datetime.strptime(data_nacimento, '%Y').date()
                except Exception:
                    self.data_nacimento = None
        elif isinstance(data_nacimento, dt.datetime):
            self.data_nacimento = data_nacimento.date()
        else:
            # assume it's already a date or None
            self.data_nacimento = data_nacimento

    def saudar(self):
        mensagem = ''

        match self.sexo.upper():
            case 'M':
                mensagem = f"Olá, meu nome é {self.nome} e eu sou o cara."
            case 'F':
                mensagem = f"Querido, meu nome é {self.nome} e eu sou linda."
            case _:
                mensagem = f"Oi, meu nome é {self.nome}."
        return mensagem
    
    def idade(self):
        if not self.data_nacimento:
            print("Data de nascimento não informada ou inválida.")
            return None

        today = dt.date.today()
        born = self.data_nacimento
        # compute age taking month/day into account
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        print(f"Tenho {age} anos.")
        return age


edy = Pessoa('Edy Junior', '16/09/1978', 'M')
print(edy.saudar())
print(edy.idade())

laila = Pessoa('Laila', '16/03/1987', 'F')
print(laila.saudar())
print(laila.idade())

zig = Pessoa('Zig', '10/11/2015', sexo='NI')
print(zig.saudar())
print(zig.idade())

