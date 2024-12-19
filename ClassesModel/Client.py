import json
from BaseClient import BaseClient
from SrviceLog import ServiceLog

class Client(BaseClient):
    def __init__(self, fullname, phone_number, male, email, age, allergic_reactions, document, id = None):
        super(Client, self).__init__(id = id, fullname=fullname, phone_number=phone_number, email=email, document=document)
        self.set_male(male)
        self.set_age(age)
        self.set_allergic_reactions(allergic_reactions)
        self.__service_logs = []

    # Классовый метод создания клиента из JSON
    @classmethod
    def from_json(data_json):
        try:
            data = json.loads(data_json)
            return Client(
                fullname=data['fullname'],
                phone_number=data['phone_number'],
                male=data['male'],
                email=data['email'],
                age=data['age'],
                allergic_reactions=data['allergic_reactions'],
                document=data['document'],
            )
        except Exception as e:
            raise ValueError("Данные JSON не верны")

    # Статические методы валидации
    @staticmethod
    def validate_male(male):
        if male not in ("М", "Ж"):
            return False
        return True

    @staticmethod
    def validate_age(age):
        if not isinstance(age, int) or age < 0:
            return False
        return True

    @staticmethod
    def validate_allergic_reactions(allergic_reactions):
        if not isinstance(allergic_reactions, str):
            return False
        return True

    # Вывод полной версии объекта
    @property
    def full_version(self):
        return (
            self.get_fullname(),
            self.get_phone_number(),
            self.get_male(),
            self.get_email(),
            self.get_age(),
            self.get_allergic_reactions(),
            self.get_document(),
        )

    # Вывод краткой версии объекта
    @property
    def short_version(self):
        return (
        self.get_fullname(),
        self.get_phone_number(),
        self.get_email(),
        self.get_document(),
        )

    def add_service_log(self, service_log):
        if isinstance(service_log, ServiceLog):
            self.__service_logs.append(service_log)
        else:
            raise TypeError("Ожидался экземпляр класса ServiceLog")

    def delete_service_log(self, service_log):
        if isinstance(service_log, ServiceLog):
            self.__service_logs.remove(service_log)
        else:
            raise TypeError("Ожидался экземпляр класса ServiceLog")

    # Getters
    def get_male(self):
        return self.__male

    def get_age(self):
        return self.__age

    def get_allergic_reactions(self):
        return self.__allergic_reactions

    def get_service_logs(self):
        return self.__service_logs

    # Setters
    def set_male(self, male):
        if super(Client, self).validate(male, self.validate_male) == False:
            raise ValueError("Пол должен быть 'М' или 'Ж'.")
        self.__male = male

    def set_age(self, age):
        if super(Client, self).validate(age, self.validate_age) == False:
            raise ValueError("Возрас не может быть отрицательным значением.")
        self.__age = age

    def set_allergic_reactions(self, allergic_reactions):
        if super(Client, self).validate(allergic_reactions, self.validate_allergic_reactions) == False:
            raise ValueError('Аллергические реакции должны быть введены строкой.')
        self.__allergic_reactions = allergic_reactions



