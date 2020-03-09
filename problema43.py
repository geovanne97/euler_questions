#colocando números testes
test_num = '1406357289'
test_num2 = '1406357285'
#método que verifica se um número é pandigital
def pandigital_number(num):
    if len(num) < 10:
        return False
#verifica se os digitos que pulam de 3 em 3 dao resto 0 para seus respectivos divisores
    if int(num[7:10]) % 17 == 0:
        if int(num[6:9]) % 13 == 0:
            if int(num[5:8]) % 11 == 0:
                if int(num[4:7]) % 7 == 0:
                    if int(num[3:6]) % 5 == 0:
                        if int(num[2:5]) % 3 == 0:
                            if int(num[1:4]) % 2 == 0:
                                return True
    return False

from itertools import permutations
#permutaçao dos digitos de 0-9
all_pandigital_number = permutations('0123456789',10)
pandigital = []
#verifico se cada permutaçao pode ser um pandigital number e print os respectivos numeros
for i in all_pandigital_number:
    num = ''.join(i)
    if pandigital_number(num):
         pandigital.append(num)
         print(num)
#faço a soma das permutaçoes que foram salvas no array pandigital
print('sum: ' + str(sum(int(num) for num in pandigital)))
