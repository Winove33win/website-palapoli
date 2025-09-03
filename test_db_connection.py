import mysql.connector
from mysql.connector import Error

def test_db_connection():
    try:
        # Configuração para conexão remota
        connection = mysql.connector.connect(
            host='168.75.84.128',  # Endereço IP do servidor
            port=3306,
            database='polapoli',
            user='polapoli',
            password='amilase1234@',
            connect_timeout=10  # Timeout de conexão em segundos
        )
        
        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"Connected to MariaDB Server version {db_info}")
            
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            record = cursor.fetchone()
            print(f"You're connected to database: {record[0]}")
            
    except Error as e:
        print(f"Error while connecting to MariaDB: {e}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MariaDB connection is closed")

if __name__ == "__main__":
    test_db_connection()
