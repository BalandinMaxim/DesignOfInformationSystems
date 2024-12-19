import uuid

class ClientRepDB:
    def __init__(self, db_connection):
        self.db = db_connection

    def get_by_id(self, client_id):
        with self.db.get_cursor() as cursor:
            cursor.execute("SELECT * FROM client WHERE id = %s", (client_id,))
            result = cursor.fetchone()
        return {
                "id": result[0],
                "fullname": result[1],
                "phone_number": result[2],
                "male": result[3],
                "email": result[4],
                "age": result[5],
                "allergic_reactions": result[6],
                "document": result[7]
            } if result else None

    def get_k_n_short_list(self, k, n):
        with self.db.get_cursor() as cursor:
            cursor.execute("""
                SELECT id, fullname, phone_number, male, email, document FROM client
                ORDER BY fullname, id LIMIT %s OFFSET %s
            """, (k, n))
            result = cursor.fetchall()
        return [
            {
                "id": row[0],
                "fullname": row[1],
                "phone_number": row[2],
                "male": row[3],
                "email": row[4],
                "document": row[5]
            }
            for row in result
        ]

    def add(self, client):
        new_id = str(uuid.uuid4())
        with self.db.get_cursor() as cursor:
            cursor.execute("""
                INSERT INTO client (id, fullname, phone_number, male, email, age, allergic_reactions, document)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (new_id, client.get_fullname(), client.get_phone_number(), client.get_male(), client.get_email(), client.get_age(), client.get_allergic_reactions(), client.get_document()))
        return new_id

    def update_by_id(self, client):
        fields = []
        values = []

        fields.append("fullname = %s")
        values.append(client.get_fullname())
        fields.append("phone_number = %s")
        values.append(client.get_phone_number())
        fields.append("male = %s")
        values.append(client.get_male())
        fields.append("email = %s")
        values.append(client.get_email())
        fields.append("age = %s")
        values.append(client.get_age())
        fields.append("allergic_reactions = %s")
        values.append(client.get_allergic_reactions())
        fields.append("document = %s")
        values.append(client.get_document())

        values.append(client.get_id())

        with self.db.get_cursor() as cursor:
            cursor.execute(f"""
                UPDATE client
                SET {', '.join(fields)}
                WHERE id = %s
            """, tuple(values))

    def delete_by_id(self, client_id):
        with self.db.get_cursor() as cursor:
            cursor.execute("DELETE FROM client WHERE id = %s", (client_id,))

    def get_count(self):
        with self.db.get_cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM client")
            result = cursor.fetchone()
        return result[0]

