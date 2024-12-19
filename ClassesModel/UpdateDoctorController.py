from Doctor import Doctor

class UpdateDoctorController:
    def __init__(self, model):
        self.model = model

    def update_doctor(self, id, fullname, activity, qualification, experience):
        # Валидация данных
        doctor = Doctor(fullname, activity, qualification, experience, id)
        self.model.update_doctor(doctor)

    def get_doctor_by_id(self, doctor_id):
        return self.model.get_doctor_by_id(doctor_id)

