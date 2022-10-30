# Importando SQLite
import sqlite3 as lite

# Criando conexão
conexao = lite.connect('Bancodedados.db')

# Criando tabela 
with conexao:
    cur = conexao.cursor()
    cur.execute("CREATE TABLE formulario( " 
                "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                "nome TEXT,"
                "email TEXT,"
                "telefone TEXT,"
                "dia_em DATE,"
                "estado TEXT,"
                "assunto TEXT)")