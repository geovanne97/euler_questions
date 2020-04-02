'''
from classe import Escritor, Caneta, MaquinaEscrever

escritor = Escritor('b')

caneta = Caneta('a')

maquina = MaquinaEscrever()

escritor.ferramenta = caneta
escritor.ferramenta.escrever()
'''
#base para um questionario
pergunta = []

p = input("digite sua pergunta:")

pergunta.append(p)
print(pergunta)
resposta = []
total = 0
for pergunta in pergunta:
    print(pergunta)


    resp = int(input("de 1 a 10, sendo 10 o mais forte, como vc sente este sintoma: "))

    resposta.append(resp)

for soma in resposta:
    total += soma
    print(total)
