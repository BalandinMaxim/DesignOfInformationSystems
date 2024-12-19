import psycopg2

class DatabaseConnection:
    _instance = None

    def __new__(cls, db_config):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance._initialize(db_config)
        return cls._instance

    def _initialize(self, db_config):
        self.connection = psycopg2.connect(
            database=db_config['dbname'],
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
        if not self.table_exists("client"):
            with self.get_cursor() as cursor:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS client (
                        id UUID PRIMARY KEY,
                        fullname VARCHAR(255) NOT NULL,
                        phone_number VARCHAR(15) NOT NULL,
                        male VARCHAR(1) CHECK (male IN ('М', 'Ж')),
                        email VARCHAR(255) NOT NULL,
                        age INTEGER CHECK (age > 0) NOT NULL,
                        allergic_reactions TEXT,
                        document VARCHAR(255) UNIQUE
                    );
                """)
                print("Таблица 'client' успешно создана.")
        else:
            print("Таблица 'client' уже существует.")

        if not self.table_exists("doctors"):
            with self.get_cursor() as cursor:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS doctors (
                    id UUID PRIMARY KEY,
                    fullname VARCHAR(255) NOT NULL UNIQUE,
                    activity VARCHAR(255) NOT NULL,
                    qualification VARCHAR(255) NOT NULL,
                    experience INTEGER CHECK (experience > 0) NOT NULL
                );
                """)
                print("Таблица 'Doctors' успешно создана.")
        else:
            print("Таблица 'Doctors' уже существует.")

        if not self.table_exists("servicelogs"):
            with self.get_cursor() as cursor:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS ServiceLogs (
                    log_id UUID PRIMARY KEY,
                    client_id UUID REFERENCES client(id) ON DELETE CASCADE,
                    doctor_id UUID REFERENCES Doctors(id) ON DELETE CASCADE,
                    name_log VARCHAR(255) NOT NULL,
                    cost INTEGER CHECK (cost > 0) NOT NULL,
                    diagnosis VARCHAR(255) NOT NULL
                );
                """)
                print("Таблица 'ServiceLogs' успешно создана.")
        else:
            print("Таблица 'ServiceLogs' уже существует.")
