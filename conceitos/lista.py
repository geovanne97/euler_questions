'''
append(),inseri elem no final da lista
insert(),inseri no começo da lista
pop(),remove o ultimo elem da lista
del(),remove elementos da lista
clear(),limpa lista
extend ou +,cocatena lista
count(),mostra qnts vezes um termo apareceu na frase
split(), vc dividi a string pelo q vc passa na funçasinno
strip(),vc tira o caracter da string
','.join(), ele junta os elementos de um array['a','b','c'] em a,b,c
enumerate(), pega cada termo da sua lista e faz o indice dela
'''

palavra = 'camiseta'
digitadas = []

while True:
    letra = input("digite alguma letra: ")

    if len(letra) > 1:
        print("Digite somente uma letra!!!")
        continue

    digitadas.append(letra)

    if letra in palavra:
        print("a letra {} tem na palavra secreta".format(letra))
    else:
        print("a letra {} nao tem na palavra secreta".format(letra))
        digitadas.pop()

    nova_palavra = ''

    for p in palavra:
        if p in digitadas:
            nova_palavra += p
        else:
            nova_palavra += '*'

    print(nova_palavra)

    if nova_palavra == palavra:
        print("acertou mizeravi")
        break
#pecorrer uma lista dentro de outra
'''
l=[['a,b'],['c','d']]
for elem in l:
    print(elem[0])
ouuuuuuuuu
for indice,valor in l:
    print(indice,valor)
'''

li = [1,2,3,4,5]
n1, n2, *n = li#n1=1,n2=2,n=[3,4,5]
#para desempacotar uma lista *li=1 2 3 4 5
print(*li,sep='-')#1-2-3-4-5

def func(*args):
    print(args)#ele transforma o q eu passar na funcao em tupla, que no caso seria (1,2,3)
    print(args[-1])#me daria o 3
    #transformar a tupla em lista pra alterar o primeiro valor dela
    args = list(args)
    args[0] = 20

func(1,2,3)

#keywords args, vc passa a chave e o valor pra funçao e ele transforma em dict
def func2(*args,**kwargs):
    print(args)
    print(kwargs)#out:{'nome':'gege',sobrenome:'saraiva'}
    #se eu quiser acessar so o nome
    print(kwargs['nome'])#ou kwargs.get('nome')

func2(*li,nome="gege",sobrenome="saraiva")
