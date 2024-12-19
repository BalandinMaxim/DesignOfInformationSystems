from Doctor import Doctor

class AddDoctorController:

    def __init__(self, model):
        self.model = model

    def add_doctor(self, fullname, activity, qualification, experience):
        # Валидация данных
        doctor = Doctor(fullname, activity, qualification, experience)
        self.model.add_doctor(doctor)

