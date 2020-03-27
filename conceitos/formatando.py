
num = 2
print(f'{num:0>5}')#out: 00005, se eu quiser colocar o 5 na esquerda coloco {num:0<5}
print(f'{num:0^5}')#out: 00500
print(f'{num:.2f}')#out: 2.00
nome=g
sobrenome=s
print('{1}'.format(nome,sobrenome))#ele vai printar o sobrenome

#editando o que deve ser mostrado na string
url = "www.google/"
print(url[:-1])#vai printar td string tirando o ultimo elemento

print(url[0:6:2])#ele vai do caracter 0 ate o 6 e pula de 2 em 2

a = ['a','b']
print(a[-1])

x=0
while x<10:
    if x == 3:
        x = x + 1
        continue ############## esse continue nao executa nada depois dele, logo na saída ele pula o numero 3
############ diferança do CONTINUE para o BREAK, o BREAK ele sai do laço de repetiçao, o CONTINUE continua executando o while
    print(x)
    x = x + 1


contador = 0
while contador < 10:
    if contador > 5#se o if entrar e der o break ele sai do laço de repetiçao e do else
        break

    contador += 1
else:
    print("numero maior que 10")

#FUNÇAO range(start=0,stop,step=1), quero ve va do 20 ou 10 de maneira decrescente range(start=20,stop=10,step=-1)
