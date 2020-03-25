from classe import Escritor, Caneta, MaquinaEscrever

escritor = Escritor('b')

caneta = Caneta('a')

maquina = MaquinaEscrever()

escritor.ferramenta = caneta
escritor.ferramenta.escrever()
