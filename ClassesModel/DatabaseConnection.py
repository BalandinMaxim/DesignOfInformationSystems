import psycopg2

class DatabaseConnection:
    """Класс для управления подключением к базе данных (Singleton)."""
    _instance = None

    def __new__(cls, db_config):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance._initialize(db_config)
        return cls._instance

    def _initialize(self, db_config):
        self.connection = psycopg2.connect(
            dbname=db_config['dbname'],
            user=db_config['user'],
            password=db_config['password'],
            host=db_config['host'],
            port=db_config['port']
        )
        self.connection.autocommit = True
        self.ensure_table_exists()

    def get_cursor(self):
        return self.connection.cursor()

    def table_exists(self, table_name):
        """Проверяет, существует ли таблица в базе данных."""
        with self.get_cursor() as cursor:
            cursor.execute("""
                SELECT EXISTS (
                    SELECT 1
                    FROM pg_catalog.pg_tables
                    WHERE tablename = %s
                );
            """, (table_name,))
            result = cursor.fetchone()
        return result[0]

    def ensure_table_exists(self):
        """Убеждается, что таблица client существует, и создает её при необходимости."""
        if not self.table_exists("client"):
            with self.get_cursor() as cursor:
                cursor.execute("""
                    CREATE TABLE client (
                        id UUID PRIMARY KEY,
                        fullname VARCHAR(255) NOT NULL,
                        phone_number VARCHAR(15) NOT NULL,
                        male VARCHAR(1) CHECK (male IN ('м', 'ж')),
                        email VARCHAR(255) NOT NULL,
                        age INTEGER CHECK (age > 0) NOT NULL,
                        allergic_reactions TEXT,
                        document VARCHAR(255) UNIQUE
                    );
                """)
                print("Таблица 'client' успешно создана.")
        else:
            print("Таблица 'client' уже существует.")
