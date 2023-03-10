class Filme:
    def __init__(self,nome,ano,duracao):
        self.nome = nome
        self.ano = ano
        self.duracao = duracao

class Serie:
    def __init__(self,nome,ano,temporadas):
        self.nome = nome
        self.ano = ano
        self.temporadas = temporadas

vingadores = Filme('Vigadores' , 2018 , 160)
print(f'Nome:{vingadores.nome} - Ano:{vingadores.ano} - Duração:{vingadores.duracao}')

atlanta = Serie('Atlanta' , 2018 , 2)
print(f'Nome:{atlanta.nome} - Ano:{atlanta.ano} - Temporada:{atlanta.temporadas}')