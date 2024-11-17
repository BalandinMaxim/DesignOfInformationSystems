import psycopg2
import uuid

class ClientRepDB:
    def __init__(self, db_config):
        self.connection = psycopg2.connect(
            dbname=db_config['dbname'],
            user=db_config['user'],
            password=db_config['password'],
            host=db_config['host'],
            port=db_config['port']
        )
        self.connection.autocommit = True

    def get_by_id(self, client_id):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM client WHERE id = %s", (client_id,))
            result = cursor.fetchone()
        return result

    def get_k_n_short_list(self, k, n):
        with self.connection.cursor() as cursor:
            offset = k * (n - 1)
            cursor.execute("""
                SELECT id, fullname, phone_number FROM client
                ORDER BY id LIMIT %s OFFSET %s
            """, (k, offset))
            result = cursor.fetchall()
        return result

    def add(self, fullname, phone_number, male, email, age, allergic_reactions, document):
        new_id = str(uuid.uuid4())
        with self.connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO client (id, fullname, phone_number, male, email, age, allergic_reactions, document)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (new_id, fullname, phone_number, male, email, age, allergic_reactions, document))
        return new_id

    def update_by_id(self, client_id, fullname=None, phone_number=None, male=None, email=None, age=None, allergic_reactions=None, document=None):
        fields = []
        values = []

        if fullname is not None:
            fields.append("fullname = %s")
            values.append(fullname)
        if phone_number is not None:
            fields.append("phone_number = %s")
            values.append(phone_number)
        if male is not None:
            fields.append("male = %s")
            values.append(male)
        if email is not None:
            fields.append("email = %s")
            values.append(email)
        if age is not None:
            fields.append("age = %s")
            values.append(age)
        if allergic_reactions is not None:
            fields.append("allergic_reactions = %s")
            values.append(allergic_reactions)
        if document is not None:
            fields.append("document = %s")
            values.append(document)

        values.append(client_id)

        with self.connection.cursor() as cursor:
            cursor.execute(f"""
                UPDATE client
                SET {', '.join(fields)}
                WHERE id = %s
            """, tuple(values))

    def delete_by_id(self, client_id):
        with self.connection.cursor() as cursor:
            cursor.execute("DELETE FROM client WHERE id = %s", (client_id,))

    def get_count(self):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM client")
            result = cursor.fetchone()
        return result[0]
