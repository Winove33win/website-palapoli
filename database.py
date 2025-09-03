import os
import sqlite3
from sqlite3 import Error

def create_connection(db_file=None):
    """Cria uma conexão com o banco de dados SQLite"""
    if db_file is None:
        # Usa o banco de dados no mesmo diretório do script
        db_file = os.path.join(os.path.dirname(__file__), 'palopoli.db')
    
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        # Habilita chaves estrangeiras
        conn.execute("PRAGMA foreign_keys = ON")
        print(f"Conectado ao SQLite {sqlite3.version}")
        return conn
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        raise

def create_tables():
    """Cria as tabelas necessárias no banco de dados"""
    sql_commands = [
        """
        CREATE TABLE IF NOT EXISTS team_members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            role TEXT NOT NULL,
            bio TEXT,
            email TEXT UNIQUE,
            phone TEXT,
            avatar_url TEXT,
            social_links TEXT,
            is_active BOOLEAN DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            slug TEXT NOT NULL UNIQUE,
            title TEXT NOT NULL,
            category TEXT NOT NULL,
            author_id INTEGER,
            reading_time INTEGER DEFAULT 3,
            cover_image TEXT,
            excerpt TEXT,
            content_html TEXT NOT NULL,
            published_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            status TEXT DEFAULT 'published' CHECK(status IN ('draft', 'published')),
            featured BOOLEAN DEFAULT 0,
            tags TEXT,
            FOREIGN KEY (author_id) REFERENCES team_members (id) ON DELETE SET NULL
        )
        """,
        # Índices para melhorar desempenho
        "CREATE INDEX IF NOT EXISTS idx_posts_status ON posts(status)",
        "CREATE INDEX IF NOT EXISTS idx_posts_featured ON posts(featured)",
        "CREATE INDEX IF NOT EXISTS idx_posts_author ON posts(author_id)",
        "CREATE INDEX IF NOT EXISTS idx_team_email ON team_members(email)"
    ]

    conn = None
    try:
        conn = create_connection()
        cursor = conn.cursor()
        
        # Executa cada comando SQL
        for command in sql_commands:
            cursor.execute(command)
        
        conn.commit()
        print("Tabelas criadas/verificadas com sucesso!")
        return True
        
    except Error as e:
        print(f"Erro ao criar tabelas: {e}")
        if conn:
            conn.rollback()
        return False
        
    finally:
        if conn:
            conn.close()

def init_db():
    """Inicializa o banco de dados criando as tabelas necessárias"""
    print("Inicializando banco de dados...")
    if create_tables():
        print("Banco de dados inicializado com sucesso!")
        return True
    else:
        print("Falha ao inicializar o banco de dados.")
        return False

if __name__ == '__main__':
    init_db()
