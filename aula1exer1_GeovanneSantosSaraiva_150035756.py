#lcarros = []

'''
Síntese:
Para executar o programa, abra o terminal e coloque o seguinte comando:
python3 aula1exer1_GeovanneSantosSaraiva_150035756.py
--------------------------------- ATENÇAO --------------------------------
na mesma pasta do código crie um arquivo chamado: arquivo.txt
'''

op = 0

def cadastrar_carro(cpf,placa,carro):
    arquivo = open("arquivo.txt", "a+")#abro o arquivo txt no modo de reescrita
    arquivo.write('{},{},{}\n'.format(cpf,placa,carro))#coloco os dados do novo carro
    arquivo.close()#fecho o arquivo para que os dados possam ser salvos

while op != 4:
    print('''    [ 1 ] cadastrar carro
    [ 2 ] pesquisar carro
    [ 3 ] deletar carro
    [ 4 ] sair''')
    op = int(input("Digite sua opção:"))

    if op == 1:
        cpf = input("Digite cpf:")
        placa = input("Digite placa:")
        carro = input("Digite carro:")
        cadastrar_carro(cpf,placa,carro)

    elif op == 2:
        cpf = input("Digite seu cpf:")

        arquivo = open("arquivo.txt", "r")#abro arquivo no modo leitura
        linhas=arquivo.readlines()#pego o que está no arquivo no formato readline
        for line in linhas:
            line.strip("\n")#tiro o \n de cada linha
            if line[0:11] == cpf:#pego só o cpf de cada linha e comparo com a entrada do usuário
                print(line)

    elif op == 3:
        dados = input("Digite cpf(11111111111),placa(abc123),carro:(fox)")
        arquivo = open("arquivo.txt", "r")
        linhas=arquivo.readlines()
        arquivo = open("arquivo.txt", "w")
        #print(linhas)
        #print(linhas[0].strip("\n"))

        for line in linhas:
            print(line)
            print(dados)
            if line.strip("\n") != dados:
                arquivo.write(line)
        arquivo.close()

    else:
        print("Valor invalido")
print("fim do programa")
