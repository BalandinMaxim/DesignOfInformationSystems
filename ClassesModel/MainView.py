import tkinter as tk
from AddUpdateClientController import AddUpdateClientController
from AddUpdateClientView import AddUpdateClientView
from tkinter import ttk, messagebox

class MainView:
    """Главное окно для отображения списка клиентов"""
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.root.title("Список клиентов")

        # Подписываем MainView на изменения модели
        self.controller.model.add_observer(self)

        # Создаем таблицу с колонками для отображения клиентов
        self.table = ttk.Treeview(
            root,
            columns=('№', 'ФИО', 'Телефон', 'Пол', 'Email', 'Документ'),
            show='headings'
        )
        self.table.heading('№', text='№')
        self.table.heading('ФИО', text='ФИО')
        self.table.heading('Телефон', text='Телефон')
        self.table.heading('Пол', text='Пол')
        self.table.heading('Email', text='Email')
        self.table.heading('Документ', text='Документ')

        self.table.pack(fill=tk.BOTH, expand=True)

        # Кнопки для добавления, изменения и удаления клиента
        button_frame = tk.Frame(root)
        button_frame.pack(fill="x",pady=10)

        add_button = tk.Button(button_frame, text="Добавить клиента", command=self.open_add_client_window)
        add_button.pack(side="left", pady=10)

        delete_button = tk.Button(button_frame, text="Удалить клиента", command=self.delete_client)
        delete_button.pack(side="left", pady=10)

        delete_button = tk.Button(button_frame, text="Скорректировать", command=self.view_details)
        delete_button.pack(side="left", pady=10)

        next_button = tk.Button(button_frame, text="Следующий", command=self.next_page)
        next_button.pack(side="right", pady=10)

        prev_button = tk.Button(button_frame, text="Предыдущий", command=self.prev_page)
        prev_button.pack(side="right", pady=10)

        self.current_page = 1
        self.page_size = 10
        self.refresh_table()  # Загрузка данных в таблицу

    def update(self, action, data):
        """Метод для обновления таблицы при изменении модели"""
        if action in ("add", "update", "delete"):
            self.refresh_table()

    def refresh_table(self):
        """Обновить таблицу с данными из модели"""
        # Удаляем старые данные из таблицы
        for row in self.table.get_children():
            self.table.delete(row)

        # Получаем данные из модели
        clients = self.controller.get_clients(self.page_size, self.current_page)
        if not clients:
            if self.controller.model.get_count() > 0:
                self.current_page -= 1
                self.refresh_table()
            print("Нет данных для отображения")
            return

        for index, client in enumerate(clients, 1):
            self.table.insert(
                '',
                'end',
                values=(
                    index + (self.current_page - 1) * 10,
                    client['fullname'],
                    client['phone_number'],
                    client['male'],
                    client['email'],
                    client['document']
                ),
                iid=client['id']  # Сохраняем ID как идентификатор строки
            )

    def open_add_client_window(self):
        """Открытие окна добавления клиента"""
        new_window = tk.Toplevel(self.root)
        AddUpdateClientView(new_window, AddUpdateClientController(self.controller.model), "add")

    def delete_client(self):
        """Удаление клиента"""
        selected_item = self.table.selection()
        if not selected_item:
            messagebox.showwarning("Ошибка", "Выберите клиента для удаления")
            return

        # Получаем ID выбранного клиента
        client_id = selected_item[0]
        self.controller.delete_client(client_id)
        messagebox.showinfo("Успех", "Клиент успешно удален!")

    def view_details(self):
        """Открытие окна с подробной информацией о клиенте для редактирования"""
        selected_item = self.table.selection()

        if not selected_item:
            messagebox.showwarning("Ошибка", "Выберите клиента для удаления")
            return

        client_id = selected_item[0]
        client_data = self.controller.model.get_client_by_id(client_id)

        if client_data:
            new_window = tk.Toplevel(self.root)
            AddUpdateClientView(new_window, AddUpdateClientController(self.controller.model), "update", client_data)
        else:
            messagebox.showwarning("Ошибка", "Не удалось найти клиента в базе данных")

    def prev_page(self):
        if self.current_page > 1:
            self.current_page -= 1
            self.refresh_table()

    def next_page(self):
        self.current_page += 1
        self.refresh_table()
