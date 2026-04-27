import mysql.connector
from mysql.connector import Error, pooling
import logging
import sys
import os

# Add parent directory to path untuk imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from settings.Config import Config

class DatabaseConnection:
    """
    Mengelola koneksi ke database MySQL dengan connection pooling
    """
    
    _connection_pool = None
    
    @staticmethod
    def init_connection_pool():
        """Inisialisasi connection pool ke MySQL"""
        try:
            config = Config()
            db_config = config.DB
            
            DatabaseConnection._connection_pool = pooling.MySQLConnectionPool(
                pool_name="livestream_pool",
                pool_size=10,
                pool_reset_session=True,
                connection_timeout=5,
                host=db_config["HOST"],
                port=db_config["PORT"],
                user=db_config["USER"],
                password=db_config["PASS"],
                database=db_config["NAME"]
            )
            logging.info("Database connection pool initialized successfully")
        except Error as err:
            logging.error(f"Error initializing database connection pool: {err}")
            raise
    
    @staticmethod
    def get_connection():
        """Dapatkan koneksi dari pool"""
        try:
            if DatabaseConnection._connection_pool is None:
                DatabaseConnection.init_connection_pool()
            
            connection = DatabaseConnection._connection_pool.get_connection()
            return connection
        except Error as err:
            logging.error(f"Error getting connection from pool: {err}")
            raise
    
    @staticmethod
    def execute_query(query: str, params: tuple = None, fetch_one: bool = False):
        """
        Eksekusi query SELECT
        
        Args:
            query: SQL query string
            params: Parameter tuple untuk prepared statement
            fetch_one: Jika True, return satu record, jika False return semua records
        
        Returns:
            List of tuples atau single tuple
        """
        connection = None
        cursor = None
        try:
            connection = DatabaseConnection.get_connection()
            cursor = connection.cursor()
            
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            
            if fetch_one:
                result = cursor.fetchone()
            else:
                result = cursor.fetchall()
            
            return result
        except Error as err:
            logging.error(f"Error executing query: {err}")
            raise
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
    
    @staticmethod
    def execute_insert(query: str, params: tuple = None):
        """
        Eksekusi query INSERT
        
        Args:
            query: SQL INSERT query string
            params: Parameter tuple untuk prepared statement
        
        Returns:
            ID dari record yang diinsert
        """
        connection = None
        cursor = None
        try:
            connection = DatabaseConnection.get_connection()
            cursor = connection.cursor()
            
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            
            connection.commit()
            return cursor.lastrowid
        except Error as err:
            if connection:
                connection.rollback()
            logging.error(f"Error inserting data: {err}")
            raise
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
    
    @staticmethod
    def execute_update(query: str, params: tuple = None):
        """
        Eksekusi query UPDATE atau DELETE
        
        Args:
            query: SQL UPDATE/DELETE query string
            params: Parameter tuple untuk prepared statement
        
        Returns:
            Jumlah rows yang di-affect
        """
        connection = None
        cursor = None
        try:
            connection = DatabaseConnection.get_connection()
            cursor = connection.cursor()
            
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            
            connection.commit()
            return cursor.rowcount
        except Error as err:
            if connection:
                connection.rollback()
            logging.error(f"Error updating/deleting data: {err}")
            raise
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
    
    @staticmethod
    def execute_many(query: str, data_list: list):
        """
        Eksekusi multiple INSERT/UPDATE sekaligus
        
        Args:
            query: SQL query string dengan placeholder
            data_list: List of tuples untuk batch execution
        
        Returns:
            Jumlah rows yang di-affect
        """
        connection = None
        cursor = None
        try:
            connection = DatabaseConnection.get_connection()
            cursor = connection.cursor()
            cursor.executemany(query, data_list)
            connection.commit()
            return cursor.rowcount
        except Error as err:
            if connection:
                connection.rollback()
            logging.error(f"Error executing batch operation: {err}")
            raise
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
    
    @staticmethod
    def test_connection():
        """Test koneksi ke database"""
        try:
            connection = DatabaseConnection.get_connection()
            if connection.is_connected():
                db_info = connection.get_server_info()
                logging.info(f"Successfully connected to MySQL Server version {db_info}")
                connection.close()
                return True
        except Error as err:
            logging.error(f"Error connecting to MySQL: {err}")
            return False


# Contoh penggunaan:
if __name__ == "__main__":
    try:
        # Test koneksi
        if DatabaseConnection.test_connection():
            print("Database connection successful!")
            
            # Contoh query
            result = DatabaseConnection.execute_query("SELECT * FROM streaming_logs LIMIT 5")
            print(result)
    except Exception as e:
        print(f"Error: {e}")
