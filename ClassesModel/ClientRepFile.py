import os
from ClientRepFileStrategy import ClientRepFileStrategy

# Класс, который использует стратегию для работы с файлами
class ClientRepFile:
    def __init__(self, strategy: ClientRepFileStrategy):
        self.strategy = strategy

    def get_all(self):
        """Получить все элементы"""
        return self.strategy.read()

    def add_entity(self, fullname, phone_number, male, email, age, allergic_reactions, document):
        """Добавить новый объект в список с новым ID"""
        # Чтение данных из файла
        data = self.strategy.read()

        # Генерация нового ID
        new_id = max([entry['id'] for entry in data], default=0) + 1
        new_entity = {
            'id': new_id,
            'fullname': fullname,
            'phone_number': phone_number,
            'male': male,
            'email': email,
            'age': age,
            'allergic_reactions': allergic_reactions,
            'document': document
        }

        # Проверка на уникальность документа
        if any(entry['document'] == document for entry in data):
            raise ValueError('Паспорт должен быть уникальным!')

        # Добавляем новый объект в список
        data.append(new_entity)

        # Записываем обновленные данные в файл
        self.strategy.write(data)

    def get_by_id(self, id):
        """Получить объект по ID"""
        data = self.strategy.read()
        for entry in data:
            if entry['id'] == id:
                return entry
        return None  # Если объект не найден

    def get_k_n_short_list(self, k, n):
        """Получить список k по счету n объектов"""
        data = self.strategy.read()
        start = (n - 1) * k
        end = start + k
        return data[start:end]

    def sort_by_field(self, field):
        """Сортировать элементы по выбранному полю"""
        data = self.strategy.read()
        if field in ["fullname", "email", "age"]:
            data.sort(key=lambda x: x.get(field))
        return data

    def replace_by_id(self, entity_id, fullname, phone_number, male, email, age, allergic_reactions, document):
        """Заменить элемент списка по ID"""
        data = self.strategy.read()
        entity = self.get_by_id(entity_id)
        if not entity:
            raise ValueError(f"Элемент с ID {entity_id} не найден.")

        # Проверка на уникальность паспорта
        if document and document != entity['document'] and any(entry['document'] == document for entry in data):
            raise ValueError('Паспорт должен быть уникальным!')

        # Обновляем данные
        if fullname:
            entity['fullname'] = fullname
        if phone_number:
            entity['phone_number'] = phone_number
            if male is not None:
                entity['male'] = male
            if email:
                entity['email'] = email
            if age:
                entity['age'] = age
            if allergic_reactions:
                entity['allergic_reactions'] = allergic_reactions
            if document:
                entity['document'] = document

            # Записываем обновленные данные в файл
            self.strategy.write(data)

    def delete_by_id(self, entity_id):
            """Удалить элемент списка по ID"""
            data = self.strategy.read()
            entity = self.get_by_id(entity_id)
            if not entity:
                raise ValueError(f"Элемент с ID {entity_id} не найден.")

            data.remove(entity)
            self.strategy.write(data)

    def get_count(self):
            """Получить количество элементов"""
            data = self.strategy.read()
            return len(data)
