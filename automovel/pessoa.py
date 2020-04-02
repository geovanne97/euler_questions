from carro import Carro

class Pessoa:
    def __init__(self,nome,cpf):
        self.nome = nome
        self.cpf = cpf
        self.carro = []

    def cadastra_carro(self,placa,modelo):
        self.carro.append(Carro(placa,modelo))

        
