from os import getenv
from dotenv import load_dotenv
import psycopg as pg

load_dotenv()

DB_HOST = getenv('HOST')
DB_PORT = getenv('PORT')
DB_USER = getenv('USER')
DB_PASSWORD = getenv('PASSWORD')
DB_NAME = getenv('DATABASE')
AUTO_COMMIT = getenv('AUTOCOMMIT')

def db_conexao():
    try:
        conexao = pg.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            dbname=DB_NAME,
            autocommit=AUTO_COMMIT
        )
        return conexao
    except Exception as erro:
        print(type(DB_HOST), DB_PORT, DB_USER, DB_PASSWORD, DB_NAME, AUTO_COMMIT)
        print(f'Erro na conexão: {erro}')
        return None