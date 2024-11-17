import json
import os
from ClientRepFileStrategy import ClientRepFileStrategy

# Стратегия работы с JSON
class ClientRepJsonStrategy(ClientRepFileStrategy):
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        """Прочитать данные из JSON файла"""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                data = json.load(f)
                return data
        return []

    def write(self, data):
        """Записать данные в JSON файл"""
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=4)
