from composicao import Cliente#n preciso colocar endereco pois ele ta instanciando dentro da classe cliente

c1 = Cliente('arnaldo',22)
c1.insere_endereco('gama','df')
print(c1.nome)
c1.lista_enderecos()
del c1

c2 = Cliente('fabin',21)
c2.insere_endereco('ceilondres','df')
c2.insere_endereco('guara','df')
c2.lista_enderecos()
print('##################')
