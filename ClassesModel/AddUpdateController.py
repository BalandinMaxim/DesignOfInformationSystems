from Client import Client

class AddUpdateClientController:

    def __init__(self, model):
        self.model = model

    def add_client(self, fullname, phone_number, male, email, document, age, allergic_reactions):
        # Валидация данных
        client = Client(fullname, phone_number, male, email, age, allergic_reactions, document)
        self.model.add_client(client)

    def update_client(self, id, fullname, phone_number, male, email, document, age, allergic_reactions):
        # Валидация данных
        client = Client(fullname, phone_number, male, email, age, allergic_reactions, document, id)
        # Если данные корректны, вызываем метод модели для корректирования клиента
        self.model.update_client(client)

    def get_client_by_id(self, client_id):
        return self.model.get_client_by_id(client_id)

