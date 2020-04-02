
from carro import Carro
from pessoa import Pessoa
import os.path

op = 0

while op != 4:
    print('''    [ 1 ] cadastrar pessoa
    [ 2 ] apagar pessoa
    [ 3 ] cadastrar carro
    [ 4 ] deletar carro
    [ 5 ] sair''')
    op = int(input("Digite sua opção:"))

    if op == 1:
        nome = input("Digite seu nome:")
        cpf = input("Digite seu cpf:")#pra saber se o cpf é numero, isnumeric(cpf)

        if isinstance(nome, str):

            p = Pessoa(nome,cpf)

            file_exists = os.path.isfile('arquivo.txt')

            if file_exists:

                arquivo = open('arquivo.txt', 'a+')
                arquivo.write('{},{}\n'.format(p.nome,p.cpf))

            else:
                arquivo = open('arquivo.txt', 'w+')
                arquivo.write('{},{}\n'.format(p.nome,p.cpf))
                arquivo.close()
                print("cadastrou")
        else:
            print("nome não pode conter um número")


    elif op == 2:
        arquivo = open("arquivo.txt", "r")
        linhas=arquivo.readlines()
        print(linhas)
        for line in linhas:
            print(line)
            a = line.split(',')
            print(a[0])
