from database_connection import create_connection

def main():
    connection = create_connection()
    cursor = connection.cursor()

    print("Acesso concluido no banco de dados")

    #Criar as tabelas

    sql = "CREATE TABLE Localização (id INT AUTO_INCREMENT PRIMARY KEY, Nome VARCHAR(50), Quantidade INT)"

    cursor.execute(sql)
    connection.commit()
    print("Criada a nova tabela ")

    close_connection(cursor, connection)

def close_connection(cursor, conexao):
    cursor.close()
    conexao.close()

if __name__ == "__main__":
    main()