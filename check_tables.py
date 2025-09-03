import sqlite3

def check_tables():
    try:
        # Conecta ao banco de dados
        conn = sqlite3.connect('palopoli.db')
        cursor = conn.cursor()
        
        # Obtém a lista de tabelas
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
        if not tables:
            print("Nenhuma tabela encontrada no banco de dados.")
        else:
            print("\nTabelas encontradas no banco de dados:")
            for table in tables:
                print(f"- {table[0]}")
                
                # Mostra a estrutura de cada tabela
                cursor.execute(f"PRAGMA table_info({table[0]});")
                columns = cursor.fetchall()
                print("  Colunas:")
                for col in columns:
                    print(f"  - {col[1]} ({col[2]})")
                print()
                
    except Exception as e:
        print(f"Erro ao verificar tabelas: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    check_tables()
