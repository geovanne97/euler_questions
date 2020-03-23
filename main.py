from pessoa import Pessoa

p2 = Pessoa('luiz', 18)

p2.teste()
'''
p2.comer('banana')
p2.parar_comer()
p2.comer('banana')
'''
p2.falar('BBB')
print(Pessoa.ano_atual)

p1 = Pessoa.por_ano_nascimento('luiz',1999)
print(p1.idade)
print(p1.gera_id())

class Produto:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    #utilizar os getter para pegar um valor e o setter para configurar esse valor, para que eu n receba string no preco
    #getter
    @property
    def preco(self):
        return self._preco

    #setter
    @preco.setter
    def preco(self, valor):#o valor no caso seria a string
        if isinstance(valor, str):#to pergundo se valor e uma instancia de string, uma classe string
            valor = float(valor.replace('R$',''))

        self._preco = valor




prod1 = Produto('blusa',100)
prod1.desconto(10)
print(prod1.preco)

prod2 = Produto('blusa','R$100')
prod2.desconto(10)
print(prod2.preco)
