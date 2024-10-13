import re


class BaseClient:
    def __init__(self, fullname, phone_number, email, document):
        self.set_fullname(fullname)
        self.set_phone_number(phone_number)
        self.set_email(email)
        self.set_document(document)

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
        if not isinstance(phone_number, str) or not re.fullmatch(r'((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}',
                                                                 phone_number):
            raise ValueError('Номер телефона введен неверно.')

        return phone_number

    @staticmethod
    def validate_email(email):
        if not isinstance(email, str) or not re.fullmatch(r'(.+)@(.+)\.(.+)', email):
            raise ValueError("Электронная поста введена неверно.")
        return email

    @staticmethod
    def validate_document(document):
        if not isinstance(document, str) or not re.fullmatch(r'^\d{4}\s\d{6}$', document):
            raise ValueError('Невреные данные паспорта (документа).')
        return document

    # Метод сравнения объектов на равенство (сравнение полей: ФИО, документ)
    def __eq__(self, other):
        if self.get_fullname() != other.get_fullname() and self.get_document() != other.get_document():
            return False

        return True

    def __ne__(self, other):
       return not(self.__eq__(self, other))

    def __hash__(self):
        return hash(self.get_fullname(), self.get_document())

    # Метод  вывода str
    def __str__(self):
        return f"Client name is {self.get_fullname()}, his/her main phone number is {self.get_phone_number()} (E-mail: {self.get_email()}, Passport: {self.get_document()})"

    # Метод  вывода repr
    def __repr__(self):
        return f"Name: {self.get_fullname()}, Phone number: {self.get_phone_number()}, E-mail: {self.get_email()}, Passport: {self.get_document()}"

    # Getters
    def get_fullname(self):
        return self.__fullname


    def get_phone_number(self):
        return self.__phone_number


    def get_email(self):
        return self.__email


    def get_document(self):
        return self.__document


    # Setters
    def set_fullname(self, fullname):
        self.__fullname = self.validate(fullname, self.validate_fullname)


    def set_phone_number(self, phone_number):
        self.__phone_number = self.validate(phone_number, self.validate_phone_number)


    def set_email(self, email):
        self.__email = self.validate(email, self.validate_email)


    def set_document(self, document):
        self.__document = self.validate(document, self.validate_document)
