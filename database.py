import sqlite3

# Funções para conectar ao banco SQLite e criar a tabela de pessoas

def conectar_banco():

    # Abre conexão com o arquivo de banco de dados local
    conexao = sqlite3.connect("banco.db")
    # Configura para acessar resultados como dicionário (coluna por nome)
    conexao.row_factory = sqlite3.Row
    return conexao

# Cria a tabela de pessoas se ela ainda não existir
def criar_tabela():
    conexao = conectar_banco()
    conexao.execute("""
    
    CREATE TABLE IF NOT EXISTS pessoas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf TEXT NOT NULL,
        setor TEXT NOT NULL                                    
    )
    """)
    # Salva as alterações no banco
    conexao.commit()
    # Fecha a conexão com o banco de dados
    conexao.close()  