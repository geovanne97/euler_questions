'''
append(),inseri elem no final da lista
insert(),inseri no começo da lista
pop(),remove o ultimo elem da lista
del(),remove elementos da lista
clear(),limpa lista
extend ou +,cocatena lista
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
