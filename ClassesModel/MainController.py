class MainController:
    """Контроллер для главного окна"""
    def __init__(self, model):
        self.model = model

    def get_clients(self, page_size, page_num):
        """Получить список клиентов для отображения на странице"""
        return self.model.get_clients(page_size, page_num)

    def delete_client(self, client_id):
        """Удалить клиента"""
        self.model.delete_client(client_id)
