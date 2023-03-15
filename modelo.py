class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def imprimir(self):
        print(f'Nome: {self._nome} - {self.ano} Ano - Likes: {self._likes}')

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    #Função que retorna o objeto como string
    def __str__(self):
        return f'Nome: {self._nome} - {self.duracao} Duração - {self.ano} Ano - Likes: {self._likes}'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    # Polimorfismo da função
    def __str__(self):
        return f'Nome: {self._nome} - {self.temporadas} Temporadas - {self.ano} Ano - Likes: {self._likes}'


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)

vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()

atlanta.dar_likes()
atlanta.dar_likes()


filmes_e_series = [vingadores, atlanta]  #Lista recebe qualquer tipo de dados

for programa in filmes_e_series:
    print(programa)