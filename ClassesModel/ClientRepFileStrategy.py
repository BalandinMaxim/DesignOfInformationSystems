import os
from abc import ABC, abstractmethod


# Абстрактный базовый класс стратегии работы с файлами
class ClientRepFileStrategy(ABC):
    @abstractmethod
    def read(self):
        """Прочитать данные из файла"""
        pass

    @abstractmethod
    def write(self, data):
        """Записать данные в файл"""
        pass
