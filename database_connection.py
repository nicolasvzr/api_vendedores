import mysql.connector
from config import db_config

def create_connection():
    db_host = db_config['host']
    db_user = db_config['user']
    db_password = db_config['password']
    db_name = db_config['database']

    conexao = mysql.connector.connect(
        host = db_host,
        user = db_user,
        password = db_password,
        database = db_name
    )

    return conexao