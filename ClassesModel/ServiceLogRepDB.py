import uuid

class ServiceLogRepDB:
    def __init__(self, db_connection):
        self.db = db_connection

    def get_by_id(self, log_id):
        with self.db.get_cursor() as cursor:
            cursor.execute("""SELECT 
                                sl.log_id,
                                sl.client_id,
                                sl.doctor_id,
                                sl.name_log,
                                sl.cost,
                                sl.diagnosis,
                                c.fullname AS client_name,
                                d.fullname AS doctor_name
                            FROM 
                                ServiceLogs AS sl
                            JOIN 
                                client AS c ON sl.client_id = c.id
                            JOIN 
                                Doctors AS d ON sl.doctor_id = d.id
                            WHERE 
                                sl.id = %s;""", (log_id,))
            result = cursor.fetchone()
        return {
                "log_id": result[0],
                "client_id": result[1],
                "doctor_id": result[2],
                "name_log": result[3],
                "cost": result[4],
                "diagnosis": result[5],
                "client_name": result[6],
                "doctor_name": result[7]
            } if result else None

    def get_k_n_short_list(self, k, n):
        with self.db.get_cursor() as cursor:

            cursor.execute("""
                SELECT log_id, client_id, doctor_id, name_log, cost, diagnosis FROM ServiceLogs
                ORDER BY name_log, log_id LIMIT %s OFFSET %s
            """, (k, n))
            result = cursor.fetchall()
        return [
            {
                "log_id": row[0],
                "client_id": row[1],
                "doctor_id": row[2],
                "name_log": row[3],
                "cost": row[4],
                "diagnosis": row[5]
            }
            for row in result
        ]

    def add(self, serviceLog):
        new_id = str(uuid.uuid4())
        with self.db.get_cursor() as cursor:
            cursor.execute("""
                INSERT INTO ServiceLogs (log_id, client_id, doctor_id, name_log, cost, diagnosis)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (new_id, serviceLog.get_client_id(), serviceLog.get_doctor().get_doctor_id(), serviceLog.get_name_log(), serviceLog.get_cost(), serviceLog.get_diagnosis()))

        return new_id

    def update_by_id(self, serviceLog):
        fields = []
        values = []

        fields.append("client_id = %s")
        values.append(serviceLog.get_client_id())
        fields.append("doctor_id = %s")
        values.append(serviceLog.get_doctor().get_doctor_id())
        fields.append("name_log = %s")
        values.append(serviceLog.get_name_log())
        fields.append("cost = %s")
        values.append(serviceLog.get_cost())
        fields.append("diagnosis = %s")
        values.append(serviceLog.get_diagnosis())

        values.append(serviceLog.get_log_id())

        with self.db.get_cursor() as cursor:
            cursor.execute(f"""
                UPDATE ServiceLogs
                SET {', '.join(fields)}
                WHERE log_id = %s
            """, tuple(values))

    def delete_by_id(self, log_id):
        with self.db.get_cursor() as cursor:
            cursor.execute("DELETE FROM ServiceLogs WHERE log_id = %s", (log_id,))

    def get_count(self):
        with self.db.get_cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM ServiceLogs")
            result = cursor.fetchone()
        return result[0]

