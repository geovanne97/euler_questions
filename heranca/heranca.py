class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} esta falando')
#alumo herda td da classe pessoa a pode colocar novas coisas nela tbm
class Aluno(Pessoa):
    def __init__(self,nome,idade,matricula):
        Pessoa.__init__(self,nome,idade)
        self.matricula = matricula


class Cliente(Pessoa):
    pass
