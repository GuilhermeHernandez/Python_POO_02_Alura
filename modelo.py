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

class playlist:
    #PROGRAMAS PODE SER UMA LISTA DE OBEJTOS REFERENTE A FILME E SERIES
    def __init__(self,nome , programas):
        self.nome = nome
        self._programas = programas

    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)

        #CRIANDO UM OBJETO QUE VAI SETTAR UMA LISTA DE PROGRAMA
        #super().__init__(programas)


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
mercenarios = Filme('mercenarios',2015,100)
atlanta = Serie('atlanta', 2018, 2)
simpsons = Serie('simpsons',2000,30)


vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()

atlanta.dar_likes()
atlanta.dar_likes()

mercenarios.dar_likes()
mercenarios.dar_likes()

simpsons.dar_likes()
simpsons.dar_likes()


filmes_e_series = [vingadores, atlanta, mercenarios, simpsons]  #Lista recebe qualquer tipo de dados

playlist_assistir = playlist('Lista de videos',filmes_e_series)

print(f'\nTamanho da playlist:{playlist_assistir.tamanho}\n')

#PARA PERCORRER A LISTA , PRECISO PASSAR O ITEM DO OBJETO
for programa in playlist_assistir.listagem:
    print(programa)

print(f'\nSimpsons esta na playlist: {simpsons in playlist_assistir.listagem}')