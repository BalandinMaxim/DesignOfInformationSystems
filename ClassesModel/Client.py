import re
import json

class Client:
    def __init__(self, client_id, fullname, phone_number, male, email, age, allergic_reactions, document):
        self.__client_id = self.validate(client_id, self.validate_client_id)
        self.__fullname = self.validate(fullname, self.validate_fullname)
        self.__phone_number = self.validate(phone_number, self.validate_phone_number)
        self.__male = self.validate(male, self.validate_male)
        self.__email = self.validate(email, self.validate_email)
        self.__age = self.validate(age, self.validate_age)
        self.__allergic_reactions = allergic_reactions 
        self.__document = document

    # Классовый метод создания клиента из JSON
    @classmethod
    def from_json(data_json):
        try:
            data = json.loads(data_json)
            return Client(
                client_id=data['client_id'],
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
    def validate_fullname(fullname):
        if not isinstance(fullname, str) or len(fullname) == 0:
            raise ValueError("ФИО введено неверно (не может быть пустым значением).")
        return fullname

    @staticmethod
    def validate_phone_number(phone_number):
         if not isinstance(phone_number, str) or not re.fullmatch(r'((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}', phone_number):
            raise ValueError('Номер телефона введен неверно.')
        return phone_number

    @staticmethod
    def validate_male(male):
        if male not in ('М', 'Ж'):
            raise ValueError("Пол должен быть 'М' или 'Ж'.")
        return male

    @staticmethod
    def validate_email(email):
        if not isinstance(email, str) or not re.fullmatch(r'(.+)@(.+)\.(.+)', email):
            raise ValueError("Электронная поста введена неверно.")
        return email

    @staticmethod
    def validate_age(age):
        if not isinstance(age, int) or age < 0:
            raise ValueError("Возрас не может быть отрицательным значением.")
        return age

    @staticmethod
    def validate_document(document):
        if not isinstance(document, str) or not re.fullmatch(r'\d{4} \d{6}', document):
            raise ValueError('Невреные данные паспорта (документа).')
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
    def get_client_id(self):
        return self.__client_id

    def get_fullname(self):
        return self.__fullname

    def get_phone_number(self):
        return self.__phone_number

    def get_male(self):
        return self.__male

    def get_email(self):
        return self.__email

    def get_age(self):
        return self.__age

    def get_allergic_reactions(self):
        return self.__allergic_reactions

    def get_document(self):
        return self.__document

    # Setters
    def set_fullname(self, fullname):
        self.__fullname = self.validate(fullname, self.validate_fullname)

    def set_phone_number(self, phone_number):
        self.__phone_number = self.validate(phone_number, self.validate_phone_number)

    def set_male(self, male):
        self.__male = self.validate(male, self.validate_male)

    def set_email(self, email):
        self.__email = self.validate(email, self.validate_email)

    def set_age(self, age):
        self.__age = self.validate(age, self.validate_age)

    def set_allergic_reactions(self, allergic_reactions):
        self.__allergic_reactions = allergic_reactions

    def set_document(self, document):
        self.__document = self.validate(document, self.validate_document)


