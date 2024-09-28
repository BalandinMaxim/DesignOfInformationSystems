import re
import json
from ClassesModel.BaseClient import BaseClient

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
            
    # Общий метод валидации
    @staticmethod
    def validate(value, validation_function):
        return validation_function(value)

    # Статические методы валидации
    @staticmethod
    def validate_male(male):
        if male not in ('М', 'Ж'):
            raise ValueError("Пол должен быть 'М' или 'Ж'.")
        return male

    @staticmethod
    def validate_age(age):
        if not isinstance(age, int) or age < 0:
            raise ValueError("Возрас не может быть отрицательным значением.")
        return age

    @staticmethod
    def validate_allergic_reactions(allergic_reactions):
        if not isinstance(allergic_reactions, str):
            raise ValueError('Аллергические реакции должны быть введены строкой.')
        return document

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

    # Метод сравнения объектов на равенство (сравнение полей: id, имя, номер телефона, email)
    def __eq__(self, other):
        if isinstance(other, Client):
            return (self.__client_id == other.__client_id and
                    self.__fullname == other.__fullname and
                    self.__phone_number == other.__phone_number and
                    self.__email == other.__email)
        return False

    # Getters
    def get_male(self):
        return self.__male

    def get_age(self):
        return self.__age

    def get_allergic_reactions(self):
        return self.__allergic_reactions

    # Setters
    def set_male(self, male):
        self.__male = self.validate(male, self.validate_male)

    def set_age(self, age):
        self.__age = self.validate(age, self.validate_age)

    def set_allergic_reactions(self, allergic_reactions):
        self.__allergic_reactions = self.validate(allergic_reactions, self.validate_allergic_reactions)
