class Observable:
    """Класс для реализации паттерна Наблюдатель"""
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        """Добавить наблюдателя"""
        self._observers.append(observer)

    def remove_observer(self, observer):
        """Удалить наблюдателя"""
        self._observers.remove(observer)

    def notify_observers(self, action, data):
        """Уведомить всех наблюдателей"""
        for observer in self._observers:
            observer.update(action, data)


class ClientModel(Observable):
    """Модель для управления клиентами"""
    def __init__(self, repository):
        super().__init__()
        self._repository = repository

    def get_clients(self, page_size, page_num):
        """Получить список клиентов для отображения на странице"""
        offset = (page_num - 1) * page_size
        return self._repository.get_k_n_short_list(page_size, offset)

    def get_client_by_id(self, client_id):
        """Получить клиента по ID"""
        return self._repository.get_by_id(client_id)

    def add_client(self, fullname, phone_number, male, email, document, age, allergic_reactions):
        """Добавить нового клиента и уведомить наблюдателей"""
        client_id = self._repository.add(
            fullname=fullname,
            phone_number=phone_number,
            male=male,
            email=email,
            document=document,
            age=age,
            allergic_reactions=allergic_reactions
        )
        self.notify_observers("add", {"id": client_id, "fullname": fullname})

    def update_client(self, client_id, fullname, phone_number, male, email, document, age, allergic_reactions):
        """Обновить данные клиента и уведомить наблюдателей"""
        self._repository.update_by_id(client_id, fullname, phone_number, male, email, document, age, allergic_reactions)
        self.notify_observers("update", {"id": client_id, "fullname": fullname})

    def delete_client(self, client_id):
        """Удалить клиента и уведомить наблюдателей"""
        self._repository.delete_by_id(client_id)
        self.notify_observers("delete", {"id": client_id})

    def get_count(self):
        return self._repository.get_count()
