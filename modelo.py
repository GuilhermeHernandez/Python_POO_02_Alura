class Filme:
    def __init__(self,nome,ano,duracao):
        self.__nome = nome
        self.ano = ano
        self.duracao = duracao
        self.__like = 0

    @property
    def nome(self):
        return self.__nome.title()

    @nome.setter
    def nome(self,novo_nome):
        self.__nome = novo_nome.title()

    @property
    def likes(self):
        return self.__like

    def dar_like (self):
        self.__like += 1


class Serie:
    def __init__(self, nome, ano, temporada):
        self.__nome = nome
        self.ano = ano
        self.temporada = temporada
        self.__like = 0

    @property
    def nome(self):
        return self.__nome.title()

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    @property
    def likes(self):
        return self.__like

    def dar_like(self):
        self.__like += 1


vingadores = Filme('vingadores',2018,160)
vingadores.dar_like()
vingadores.nome = 'Mercenarios'

print(f'Nome do filme: {vingadores.nome} - Ano : {vingadores.ano} - Duração : {vingadores.duracao}')
print(f'Quantidade de likes : {vingadores.likes}')


rick = Serie('Rick and Morty',2019,6)
rick.dar_like()

print(f'Nome do filme: {rick.nome} - Ano : {rick.ano} - Temporada : {rick.temporada}')
print(f'Quantidade de likes : {rick.likes}')
