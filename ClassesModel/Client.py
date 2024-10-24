import re
import json
from BaseClient import BaseClient

class Client(BaseClient):
    def __init__(self, fullname, phone_number, male, email, age, allergic_reactions, document):
        super(Client, self).__init__(fullname=fullname, phone_number=phone_number, email=email, document=document)
        self.set_male(male)
        self.set_age(age)
        self.set_allergic_reactions(allergic_reactions)

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
        if male not in ('М', 'Ж'):
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

    # Getters
    def get_male(self):
        return self.__male


    def get_age(self):
        return self.__age


    def get_allergic_reactions(self):
        return self.__allergic_reactions

    # Setters
    def set_male(self, male):
        if super().validate(male, self.validate_male):
            raise ValueError("Пол должен быть 'М' или 'Ж'.")
        self.__male = male


    def set_age(self, age):
        if super().validate(age, self.validate_age):
            raise ValueError("Возрас не может быть отрицательным значением.")
        self.__age = age


    def set_allergic_reactions(self, allergic_reactions):
        if super().validate(allergic_reactions, self.validate_allergic_reactions):
            raise ValueError('Аллергические реакции должны быть введены строкой.')
        self.__allergic_reactions = allergic_reactions
