'''
public: posso manipular o atributo de qualquer lugar
protected: self._dados ele nao mostra no complemento automatico, isso me diz que é um atributo q so deve ser manipulado dentro da classe
mas eu ainda consigo mudar o valor dele e quebrar o codigo de fora da classe, self.dados = 'oi'
private: self.__dados, se eu fizer self.__dados = 'oi' a estrutura definida no __init__ nao e modificada, logo
é criado um atributo com o mesmo nome, mas o tipo de dado que é dict nao muda
agora se eu colocar print(bd.__dados) ele me mostra 'oi', que é o atributo que ele criou para n mudarf o que ta definido na classmethod
pra eu acessa os dados reais daquela instancia seria: bd._BaseDeDados__dados
'''

class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    #mudar o acesso de __dados para _dados
    '''
    @property
    def dados(self):
        return __dados
'''
    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}#clientes é a chave do dict{id:nome}, {'clientes': {1: 'a'}}
        else:
            self.__dados['clientes'].update({id:nome})

    def lista_clientes(self):
        print(bd.__dados)
        for id, nome in self.__dados['clientes'].items():

            print(id,nome)

    def apaga_clientes(self,id):
        del self.__dados['clientes'][id]
        print('apagou')

bd = BaseDeDados()
bd.inserir_cliente(1,'a')
bd.inserir_cliente(2,'b')

#como o atributo esta protegido se eu colocar
#print(bd.__dados)ele vai quebrar

bd.lista_clientes()
#ele cria uma variavel com o mesmo nome do atributo definido na classe, para proteger e tornar privado o dado
bd.__dados = 'oi'
print(bd.__dados)

print(bd._BaseDeDados__dados)#desse jeito vc poderia mudar o tipo desse atributo
