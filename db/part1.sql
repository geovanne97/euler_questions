-- SELECT * FROM Taxi WHERE AnoFab > 2000

--LIKE
SELECT ...
  FROM nome_tabela
    WHERE condicao
      LIKE expressao regular
essa expressao regular seria pra eu achar na linha uma dado com um padrao
exemplo:
% é qualquer caracter com 0 a n caracteres
_ exatamente um caracter
= caracter de escape, ele mostra o que vc quer receber em tal caracter, tipo um = _,quero receber um underscore
questao
1)selecionar placas que comecem com DK
SELECT *
FROM Taxi
WHERE placa LIKE DK%
2)placas com 7 na penultima posiçao
SELECT *
FROM Taxi
WHERE placa LIKE %7_

--AS, serve para dar apelido as tabelas
SELECT Cl.Nome,Co.Placa
FROM Cliente AS Cl, Corrida AS Co;

--usar o AS para renomear os campos
SELECT Cl.nome AS nome_cliente
FROM Cliente AS Cl;

-- DISTINCT é qnd eu n quero  que retorne tuplas repetidas, pq qnd fazemos projeçao
--pode ser que haja tuplas com os mesmos valores nas colunas selecionadas
--como pode ter duas crianças com a mesma mae eu uso o DISTINCT
-- qnd eu coloco DISTINCT com duas colunas ele vai considerar q o conjuntos dessas 2 colunas que t q ser diferente
SELECT DISTINCT nome_da_mae FROM Pessoa

-- ORDER BY,vem depois do WHERE
ORDER BY Nome,Modelo;

--produto cartesiano
-- cria uma nova tabela para visualizaçao, onde a tupla da primeira coluna se conecta com tds as linhas
-- da segunda tabela, logo se eu tiver uma tabela1 com 2 linhas e a tabela2 com 3 linhas a nova tabela
-- terá 6 linhas
--logo nesse exemplo de baixo terá 6 linhas
SELECT CL.Id, CL.Nome, Co.Id_carro, Co.Placa, Co.Modelo
  FROM Cliente Cl, Corrida Co


-- join
-- inner join, ele vai trazer a tupla da esquerda caso tenha conexao c a linha da direita
-- left join, ele vai trazer a tupla da esquerda independente de existir a FK do outro lado
-- right join
-- full join traz tds as tuplas, é um tipo de produto cartesiano

--exemplo inner join
SELECT Cli.CliID, Cli.Nome, Cor.Placa, Cor.DataPedido
  FROM Cliente Cli
  INNER JOIN Corrida AS Cor ON Cli.CliID = Cor.CliID;--aqui basicamente eu coloco a condiçao de que a pk de
--um tem que ta na fk de outro, ele só vai colocar as tuplas que tiverem essa conexao
--agora se eu trocar o INNER JOIN por LEFT JOIN tds as tuplas da esquerda aparecerao e placa e DataPedido
--vao aparecer se tiver com a condiçao satisfeita, ai as tuplas da esquerda que nao tiverem com valores das
--tuplas da direita vai aparecer o valor Null


--DELETE
DELETE FROM Corrida Co
  WHERE Co.Placa = 'ABC123'

--UPDATE
UPDATE Taxi T
  SET T.AnoFab = 2002;
  WHERE T.Placa = 'abc123';

--GROUP BY
SELECT T.Modelo, COUNT(*) AS Numero--eu vejo qnts modelos tem por nome específico,renomeio essa nova coluna para Numero
FROM Taxi T
GROUP BY T.Modelo;--isso faz o mesmo que o DISTINCT
