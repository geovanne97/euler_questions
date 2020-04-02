class Escritor:
    def __init__(self,nome):
        self.__nome = nome #fazendo com q o atributo nao possa ser acessado fora da classe
        self.__ferramenta  = None

    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self,ferramenta):
        self.__ferramenta = ferramenta

class Caneta:
    def __init__(self,marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print('escrevendo')

class MaquinaEscrever:

    def escrever(self):
        print('maquina escrevendo')
