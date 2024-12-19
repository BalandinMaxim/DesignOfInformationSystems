class Doctor:
    def __init__(self, fullname, activity, qualification, experience, doctor_id=None):
        self.__doctor_id = doctor_id
        self.set_fullname(fullname)
        self.set_activity(activity)
        self.set_qualification(qualification)
        self.set_experience(experience)

    @staticmethod
    def validateOfNumbers(value):
        return isinstance(value, int) and value >= 0

    @staticmethod
    def validateOfStringValue(value):
        return isinstance(value, str) and len(value) > 0

    # Getters and Setters
    def get_doctor_id(self):
        return self.__doctor_id

    def get_fullname(self):
        return self.__fullname

    def set_fullname(self, value):
        if self.validateOfStringValue(value):
            self.__fullname = value
        else:
            raise ValueError("ФИО введено неверно (не может быть пустым значением).")

    def get_activity(self):
        return self.__activity

    def set_activity(self, value):
        if self.validateOfStringValue(value):
            self.__activity = value
        else:
            raise ValueError("Род деятельности введен неверно (не может быть пустым значением).")

    def get_qualification(self):
        return self.__qualification

    def set_qualification(self, value):
        if self.validateOfStringValue(value):
            self.__qualification = value
        else:
            raise ValueError("Квалификация введена неверно (не может быть пустым значением).")

    def get_experience(self):
        return self.__experience

    def set_experience(self, value):
        if self.validateOfNumbers(value):
            self.__experience = value
        else:
            raise ValueError("Опыт (количество лет) введен неверно (не может быть отрицательным значением).")

    def __eq__(self, other):
        if isinstance(other, Doctor):
            return self.__fullname == other.__fullname
        return False

    def __repr__(self):
        return f"Doctor({self.get_fullname()}, {self.get_activity()}, {self.get_qualification()}, {self.get_experience()} years)"
