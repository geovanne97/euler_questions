from random import randint

class Pessoa:
    #isso aqui sao atributos da classe pessoa
    ano_atual = 2020
    #isso aqui sao atributos da instancia
    def __init__(self,nome,idade,comendo=False,falando=False):#e aqui teria que colocar variavel tbm
        #isso faz com que todos os metodos da classe pessoa acesse esses atributos
        self.nome = nome
        self.idade=idade
        self.comendo=comendo
        self.falando=falando
        #caso eu queira que somente esse metodo tenha acesso a um atributo eu coloco assim
        #variavel = variavel

    def teste(self):
        print(self.nome,self.comendo)

    def falar(self,assunto):
        if self.comendo:
            print(f'{self.nome} nao pode falar comendo')
            return

        if self.falando:
            print(f'{self.nome} ja está falando')
            return

        print(f'{self.nome} está falando sobre {assunto}')
        self.falando = True

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} ja esta comendo')
            return

        print(f'{self.nome} esta comendo {alimento}')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} nao esta comendo')
            return

        print(f'{self.nome} parou de comer')
        self.comendo = False

    @classmethod#decorator que mostra que é um metodo de classe nao de instancia, ele recebe uma classe
    def por_ano_nascimento(cls,nome,ano_nascimento):
        idade = cls.ano_atual - ano_nascimento #tenho que colocar cls.ano_atual pra mostrar que e atrib de classe
        return cls(nome,idade)

    @staticmethod#mostra que o metodo nao tem que receber nem uma instancia nem uma classe
    def gera_id():
        rand = randint(10000,19999)
        return rand
