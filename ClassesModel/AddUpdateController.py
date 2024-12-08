from Client import Client

class AddUpdateClientController:
    """Контроллер для добавления клиента"""

    def __init__(self, model):
        self.model = model

    @staticmethod
    def validate_data(fullname, phone_number, male, email, document, age, allergic_reactions):
        """Использует функции из Client и BaseClient для валидации данных"""
        errors = []
        if not Client.validate_fullname(fullname):
            errors.append("ФИО не может быть пустым или некорректным.")
        if not Client.validate_phone_number(phone_number):
            errors.append("Некорректный номер телефона.")
        if not Client.validate_male(male):
            errors.append("Пол должен быть указан как 'М' или 'Ж'.")
        if not Client.validate_email(email):
            errors.append("Некорректный email.")
        if not Client.validate_document(document):
            errors.append("Документ должен быть корректным.")
        if not Client.validate_age(age):
            errors.append("Возраст должен быть положительным числом.")
        if not Client.validate_allergic_reactions(allergic_reactions):
            errors.append("Аллергические реакции должны быть корректной строкой.")

        if errors:
            raise ValueError("\n".join(errors))

    def add_client(self, fullname, phone_number, male, email, document, age, allergic_reactions):
        """Добавить клиента после валидации"""
        # Валидация данных
        self.validate_data(fullname, phone_number, male, email, document, age, allergic_reactions)

        # Если данные корректны, вызываем метод модели для добавления клиента
        self.model.add_client(
            fullname=fullname,
            phone_number=phone_number,
            male=male,
            email=email,
            document=document,
            age=age,
            allergic_reactions=allergic_reactions
        )

    def update_client(self, id, fullname, phone_number, male, email, document, age, allergic_reactions):
        """Добавить клиента после валидации"""
        # Валидация данных
        self.validate_data(fullname, phone_number, male, email, document, age, allergic_reactions)

        # Если данные корректны, вызываем метод модели для корректирования клиента
        self.model.update_client(
            client_id=id,
            fullname=fullname,
            phone_number=phone_number,
            male=male,
            email=email,
            document=document,
            age=age,
            allergic_reactions=allergic_reactions
        )
