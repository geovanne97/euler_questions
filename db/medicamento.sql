-- relaçao MEDICAMENTO 1:n VIRUS_A
CREATE TABLE Medicamento(
  Nome_Venda VARCHAR(50),
  Composto_Ativo VARCHAR(50) NOT NULL,
  PRIMARY KEY(Nome_Venda)
);

INSERT INTO Medicamento VALUES ("dipirona","virulex");
INSERT INTO Medicamento VALUES ("OutroSol", "virulex");
INSERT INTO Medicamento VALUES ("QualquerZona", "H1Nex");
INSERT INTO Medicamento VALUES ("OutraZona", "H1Nex");
INSERT INTO Medicamento VALUES ("Novalgina", "H1Nex");


CREATE TABLE VirusA(
  Nome_Cientifico VARCHAR(50),
  Nome_Popular VARCHAR(50) NOT NULL,
  Incubacao INTEGER,
  Medicamento_Trata VARCHAR(50),
  PRIMARY KEY(Nome_Cientifico),
  FOREIGN KEY(Medicamento_Trata)--primeiro eu coloco qual atributo da tabela virusA é o fk
    REFERENCES Medicamento(Nome_Venda)--agora eu coloca a tabela de onde vou herdar a FK e o nome do atributo PK
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);

INSERT INTO VirusA  VALUES ("HJN3", "Gripe Barataria", 20, "QualquerZona");--o ultimo atributo tem que existir na tabela medicamento, já que é um FK
INSERT INTO VirusA VALUES ("H4N5", "Gripe Transitoria", 5, "QualquerZona");
INSERT INTO VirusA VALUES ("H7N3", "Gripe Matadora", 2, "OutraZona");
INSERT INTO VirusA VALUES ("H7N3", "Gripe Matadora", 2, "Novalgina");

--relaçao MEDICAMENTO n:n VIRUS_B, ou seja, terei que colocar uma tabela extra da relaçao entra
--as duas entidades
CREATE TABLE VirusB(
  Nome_Cientifico VARCHAR(50),
  Nome_Popular VARCHAR(50) NOT NULL,
  Incubacao INTEGER,
  PRIMARY KEY(Nome_Cientifico)
);

--agora criar a tabela intermediaria
CREATE TABLE Trata(
  Nome_Cientifico_Virus VARCHAR(50),
  Medicamento_Trata VARCHAR(50),
  FOREIGN KEY(Nome_Cientifico_Virus)--primeiro eu coloco qual atributo da tabela virusB é o fk
    REFERENCES VirusB(Nome_Cientifico)--agora eu coloca a tabela de onde vou herdar a FK e o nome do atributo PK
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
  FOREIGN KEY(Medicamento_Trata)--primeiro eu coloco qual atributo da tabela virusA é o fk
    REFERENCES Medicamento(Nome_Venda)--agora eu coloca a tabela de onde vou herdar a FK e o nome do atributo PK
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);

INSERT INTO VirusB VALUES ("HJN3", "Gripe Barataria", 20);
INSERT INTO VirusB VALUES ("H4N5", "Gripe Transitoria", 5);
INSERT INTO VirusB VALUES ("H7N3", "Gripe Matadora", 2);

INSERT INTO Trata VALUES ("HJN3", "QualquerSol");
INSERT INTO Trata VALUES ("H4N5", "QualquerSol");
INSERT INTO Trata VALUES ("H7N3", "OutraZona");

-- Exercicio 4 - Compostos ativos disponiveis
SELECT Composto_Ativo FROM Medicamento;

-- Exercicio 5a - nome popular dos vírusA tratados pelo medicamento de nome de venda Nome de Venda
SELECT Nome_Popular
  FROM VirusA
  WHERE Medicamento_Trata = 'Novalgina';

-- Exercicio 5b - nome popular dos vírus tratados pelo medicamento de composto ativo virulex
SELECT V.Nome_Popular
  FROM VirusA V, Medicamento M
  WHERE V.Medicamento_Trata = M.Nome_Venda AND M.Composto_Ativo = 'virulex';

-- Exercicio 6 - nome popular dos vírusB tratados pelo medicamento de composto ativo X
SELECT V.Nome_Popular
  FROM VirusB V, Trata T, Medicamento M
  WHERE V.Nome_Cientifico = T.Nome_Cientifico_Virus AND M.Nome_Venda = T.Medicamento_Trata
  AND M.Composto_Ativo = 'virulex'

  -- Media de incubacao dos virus
  SELECT AVG(Incubacao) FROM VIRUS_B;

  -- Exercicio 7a - Quantos vírusA sao tratados por cada medicamento
SELECT M.Medicamento_Trata, COUNT(*)
  FROM Medicamento M, VirusA V
  GROUP BY M.Medicamento_Trata;

  -- Exercicio 7b - Quantos vírus trata cada composto ativo
  SELECT M.Composto_Ativo, COUNT(*)
         FROM VirusA V, Medicamento M
         WHERE V.Medicamento_Trata = M.Nome_Venda
         GROUP BY M.Composto_Ativo;

  -- Exercicio 8a - Quantos vírusB trata cada medicamento,a tabela trata vai ter todos os
  -- medicamentos e quais doenças ele trata
SELECT T.Medicamento_Trata, COUNT(*)
  FROM Trata T
  GROUP BY T.Medicamento_Trata;

  -- Exercicio 8b - Quantos vírusB trata cada composto ativo
SELECT M.Composto_Ativo,COUNT(*)
  FROM Medicamento M, Trata T
  WHERE T.Medicamento_Trata = M.Nome_Venda--seleciono as tuplas
  GROUP BY M.Composto_Ativo

-- qnts compostos ativos que tratam virusA com incubaçao > 5
SELECT M.Composto_Ativo, COUNT(*)
  FROM Medicamento M, VirusA V
  WHERE M.Nome_Venda = V.Medicamento_Trata AND V.Incubacao > 5
  GROUP BY M.Composto_Ativo

  -- qnts compostos ativos que tratam virusB com incubaçao > 5
  SELECT M.Composto_Ativo, COUNT(*) Numero_Virus
         FROM VirusA V, Medicamento M
         WHERE V.Medicamento_Trata = M.Nome_Venda
         GROUP BY M.Composto_Ativo
         HAVING Numero_Virus > 5;

-- Extensões da Questao
SELECT M.Composto_Ativo, COUNT(*), AVG(Incubacao), MIN(Incubacao), MAX(Incubacao)
      FROM VirusA V, Medicamento M
      WHERE V.Medicamento_Trata = M.Nome_Venda
      GROUP BY M.Composto_Ativo;

--virusB tratados pelo composto ativo virulex
SELECT V.Nome_Popular
  FROM VirusB V
  WHERE V.Nome_Cientifico
      IN(
        SELECT T.Nome_Cientifico_Virus
          FROM Trata T, Medicamento M
          WHERE T.Medicamento_Trata = M.Nome_Venda AND M.Composto_Ativo = 'virulex'
      );
--pra saber os virus que nao sao tratador por virulex é so colocar NOT IN

--selecionar o nome popular dos virus tratados pelo composto ativo virulex, n:n
SELECT V.Nome_Popular
  FROM VIRUS_B V, Medicamento M, Trata T
  WHERE V.Nome_Cientifico = T.Nome_Cientifico_Virus AND M.Nome_Venda = T.Medicamento_Trata
  AND M.Composto_Ativo = 'virulex';

--no where eu conecto as tabelas, qnd faço isso cada linha da tabela trata vai ter os atributos da tabela
--medicamento e virus
--tds os virus q tem pelo menos um medicamento pra tratar ele
  SELECT V.Nome_Popular
         FROM VirusB V
         WHERE EXISTS (
            SELECT M.Composto_Ativo FROM
                   Trata T, Medicamento M
                   WHERE T.Medicamento_Trata = M.Nome_Venda AND
                         T.Nome_Cientifico_Virus = V.Nome_Cientifico);--vou pegar o nome cientifico
                         --do nome popular que apareceu no select de fora e faze a comparaçao

--saber o composto ativo que nao trata gripe Barataria VirusA
SELECT M.Composto_Ativo
  FROM Medicamento M
  WHERE M.Nome_Venda NOT IN(
    SELECT V.Medicamento_Trata
    FROM VirusA V
    WHERE V.Nome_Popular = 'Gripe Barataria'
  );

  SELECT DISTINCT M.Composto_Ativo
       FROM Medicamento M
       WHERE M.Composto_Ativo NOT IN (
          SELECT DISTINCT M2.Composto_Ativo FROM
                 Medicamento M2, VirusA V
                 WHERE M2.Nome_Venda = V.Medicamento_Trata AND
                       V.Nome_Popular = "Gripe Barataria");
