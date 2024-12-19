from SrviceLog import ServiceLog
from Doctor import Doctor

class AddServiceController:
    def __init__(self, model):
        self.model = model

    def add_service(self, name_log, cost, diagnosis, doctor_id, client_id, doctor_name):
        # Валидация данных
        doctor = Doctor(doctor_name,"doctor", "qualification", 1, doctor_id)
        serviceLog = ServiceLog(client_id, doctor, name_log, cost, diagnosis)
        self.model.add_service(serviceLog)

