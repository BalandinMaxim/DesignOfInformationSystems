import re

class Client:
    def __init__(self, client_id, fullname, phone_number, male, email, age, allergic_reactions, document):
        self.__client_id = client_id
        self.__fullname = fullname
        self.__phone_number = phone_number
        self.__male = male
        self.__email = email
        self.__age = age
        self.__allergic_reactions = allergic_reactions
        self.__document = document

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
        self.__fullname = fullname

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def set_male(self, male):
        self.__male = male

    def set_email(self, email):
        self.__email = email

    def set_age(self, age):
        self.__age = age

    def set_allergic_reactions(self, allergic_reactions):
        self.__allergic_reactions = allergic_reactions

    def set_document(self, document):
        self.__document = document
