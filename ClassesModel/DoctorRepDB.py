import uuid

class DoctorRepDB:
    def __init__(self, db_connection):
        self.db = db_connection

    def get_by_id(self, doctor_id):
        with self.db.get_cursor() as cursor:
            cursor.execute("SELECT * FROM Doctors WHERE id = %s", (doctor_id,))
            result = cursor.fetchone()
        return {
                "id": result[0],
                "fullname": result[1],
                "activity": result[2],
                "qualification": result[3],
                "experience": result[4]
            } if result else None

    def get_k_n_short_list(self, k, n):
        with self.db.get_cursor() as cursor:
            cursor.execute("""
                SELECT id, fullname, activity FROM Doctors
                ORDER BY fullname, id LIMIT %s OFFSET %s
            """, (k, n))
            result = cursor.fetchall()
        return [
            {
                "id": row[0],
                "fullname": row[1],
                "activity": row[2]
            }
            for row in result
        ]

    def add(self, doctor):
        new_id = str(uuid.uuid4())

        with self.db.get_cursor() as cursor:
            cursor.execute("""
                INSERT INTO Doctors (id, fullname, activity, qualification, experience)
                VALUES (%s, %s, %s, %s, %s)
            """, (new_id, doctor.get_fullname(), doctor.get_activity(), doctor.get_qualification(), doctor.get_experience()))
        return new_id

    def update_by_id(self, doctor):
        fields = []
        values = []

        fields.append("fullname = %s")
        values.append(doctor.get_fullname())
        fields.append("activity = %s")
        values.append(doctor.get_activity())
        fields.append("qualification = %s")
        values.append(doctor.get_qualification())
        fields.append("experience = %s")
        values.append(doctor.get_experience())

        values.append(doctor.get_doctor_id())

        with self.db.get_cursor() as cursor:
            cursor.execute(f"""
                UPDATE Doctors
                SET {', '.join(fields)}
                WHERE id = %s
            """, tuple(values))

    def delete_by_id(self, doctor_id):
        with self.db.get_cursor() as cursor:
            cursor.execute("DELETE FROM Doctors WHERE id = %s", (doctor_id,))

    def get_count(self):
        with self.db.get_cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM Doctors")
            result = cursor.fetchone()
        return result[0]

