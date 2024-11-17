import json
import os
from ClientRepFileStrategy import ClientRepFileStrategy

# Стратегия работы с YAML
class ClientRepYamlStrategy(ClientRepFileStrategy):
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        """Прочитать данные из YAML файла"""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                data = yaml.safe_load(f)
                return data
        return []

    def write(self, data):
        """Записать данные в YAML файл"""
        with open(self.filename, 'w') as f:
            yaml.dump(data, f, default_flow_style=False)
