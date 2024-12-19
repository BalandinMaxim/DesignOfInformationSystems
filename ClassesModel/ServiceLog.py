from Doctor import Doctor

class ServiceLog:
    def __init__(self, client_id, doctor, name_log, cost, diagnosis, log_id=None):
        self._log_id = log_id
        self._client_id = client_id
        self._doctor = doctor  # Instance of Doctor
        self._name_log = name_log
        self._cost = cost
        self._diagnosis = diagnosis

    @staticmethod
    def validateOfNumbers(value):
        return isinstance(value, int) and value >= 0

    @staticmethod
    def validateOfStringValue(value):
        return isinstance(value, str) and len(value) > 0

    # Getters and Setters
    def get_log_id(self):
        return self._log_id

    def get_client_id(self):
        return self._client_id

    def get_doctor(self):
        return self._doctor

    def set_doctor(self, value):
        if isinstance(value, Doctor):
            self._doctor = value
        else:
            raise ValueError("Докутор должен принадлежать классу Doctor")

    def get_name_log(self):
        return self._name_log

    def set_name_log(self, value):
        if Doctor.validateOfStringValue(value):
            self._name_log = value
        else:
            raise ValueError("Название услуги введено неверно (не может быть пустым значением).")

    def get_cost(self):
        return self._cost

    def set_cost(self, value):
        if Doctor.validateOfNumbers(value):
            self._cost = value
        else:
            raise ValueError("Стоимость услуги введена неверно (не может быть отрицательным значением).")
    def get_diagnosis(self):
        return self._diagnosis

    def set_diagnosis(self, value):
        if Doctor.validateOfStringValue(value):
            self._diagnosis = value
        else:
            raise ValueError("Диагноз введен неверно (не может быть пустым значением).")

    def __repr__(self):
        return (f"ServiceLog(Log ID: {self.get_log_id()}, Client ID: {self.get_client_id()}, "
                f"Doctor: {self.get_doctor().get_fullname()}, Service: {self.get_name_log()}, "
                f"Cost: {self.get_cost()}, Diagnosis: {self.get_diagnosis()})")
