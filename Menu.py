from CRUD import *

while (True and not False):
    print('''
    +-------------------------------------------------------------+
    |                  CRUD - Python com SQLite3                  |
    | 1. Create (Inserir dado em uma tabela)                      |
    | 2. Read (Select, lista os dados de uma tabela)              |
    | 3. Update (Atualiza uma tupla ou um atributo)               |
    | 4. Delete (Remove uma tupla de uma tabela)                  |
    | 5. Criar Tabela                                             |
    | Input < 1 or > 5 or != Numbers. Sair                        |
    | Use os comandos do SQLite3!                                 |
    +-------------------------------------------------------------+
    ''')
    foo = input('Selecione uma opção: ')
    if foo == '1':
        sql = input("Digite o comando para INSERIR: ")
        inserir(sql)
        #Exemplo inserir("INSERT INTO BLOCKCHAIN VALUES(4, 'Teste')")
    elif foo == '2':
        sql = input("Digite o comando SELECT: ")
        select(sql)
        time.sleep(5)
        #Exemplo select("SELECT * FROM BLOCKCHAIN")
    elif foo == '3':
        sql = input("Digite o comando do UPDATE: ")
        update(sql)
        #Exemplo update("UPDATE BLOCKCHAIN SET NOME = 'KKKK' WHERE ID = 1")
    elif foo == '4':
        sql = input("Digite o comando do DELETE: ")
        remove(sql)
        #Exemplo delete("DELETE FROM BLOCKCHAIN WHERE ID = 1")
    elif foo == '5':
        sql = input("Digite o comando para criar a Tabela: ")
        criarTabela(sql)
    else:
        c.close()
        conn.close()
        print("Encerrado")
        exit(0)