from CRUD import *
import random

criarTabela("CREATE TABLE IF NOT EXISTS BLOCKCHAIN (id INTEGER PRIMARY KEY, nome TEXT)")
inserir("INSERT INTO BLOCKCHAIN(nome) VALUES ('Fulano')")
inserir("INSERT INTO BLOCKCHAIN(nome) VALUES ('Ciclano')")
inserir("INSERT INTO BLOCKCHAIN(nome) VALUES ('Deltrano')")

select("SELECT * FROM BLOCKCHAIN WHERE ID = 2")
print()
select("SELECT * FROM BLOCKCHAIN")

update("UPDATE BLOCKCHAIN SET NOME = 'Ciclano da Silva' WHERE ID = 2")

remove("DELETE FROM BLOCKCHAIN WHERE ID = 1")