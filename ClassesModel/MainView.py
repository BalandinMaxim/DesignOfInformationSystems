import tkinter as tk
from tkinter import ttk

class MainView:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.root.title("Платная поликлинника")

        # Подписываем MainView на изменения модели
        self.controller.model.add_observer(self)

        notebook = ttk.Notebook(root)
        notebook.pack(fill=tk.BOTH, expand=True)

        # Вкладка для клиентов
        self.clients_tab = ttk.Frame(notebook)
        notebook.add(self.clients_tab, text="Клиенты")

        # Вкладка для докторов
        self.doctors_tab = ttk.Frame(notebook)
        notebook.add(self.doctors_tab, text="Докторы")

        # Создаем таблицу с колонками для отображения клиентов для вкладки Клиенты
        self.client_table = ttk.Treeview(
            self.clients_tab,
            columns=('№', 'ФИО', 'Телефон', 'Пол', 'Email', 'Документ'),
            show='headings'
        )
        self.client_table.heading('№', text='№')
        self.client_table.heading('ФИО', text='ФИО')
        self.client_table.heading('Телефон', text='Телефон')
        self.client_table.heading('Пол', text='Пол')
        self.client_table.heading('Email', text='Email')
        self.client_table.heading('Документ', text='Документ')

        self.client_table.pack(fill=tk.BOTH, expand=True)

        self.client_current_page = 1
        self.client_page_size = 10
        self.refresh_clients_table()  # Загрузка данных в таблицу

        # Кнопки для добавления, изменения и удаления клиента
        button_frame = tk.Frame(self.clients_tab)
        button_frame.pack(fill="x", pady=10)

        add_client_button = tk.Button(button_frame, text="Добавить клиента", command=lambda: controller.open_add_client_window(self.controller, self.root))
        add_client_button.pack(side="left", pady=10)

        delete_client_button = tk.Button(button_frame, text="Удалить клиента", command=lambda: controller.delete_client(self.client_table))
        delete_client_button.pack(side="left", pady=10)

        delete_client_button = tk.Button(button_frame, text="Скорректировать", command=lambda: controller.view_details(self.client_table, self.root, self.controller))
        delete_client_button.pack(side="left", pady=10)

        next_client_button = tk.Button(button_frame, text="Следующий", command=self.next_client_page)
        next_client_button.pack(side="right", pady=10)

        prev_client_button = tk.Button(button_frame, text="Предыдущий", command=self.prev_client_page)
        prev_client_button.pack(side="right", pady=10)

        show_serviceLogsByClient_buuton = tk.Button(button_frame, text="Предоставляемые клиенту услуги", command=lambda: controller.showServiceLogs_details(self.client_table, self.root))
        show_serviceLogsByClient_buuton.pack(side="left", pady=10)

        # Создаем таблицу с колонками для отображения клиентов для вкладки Докторы
        self.doctors_table = ttk.Treeview(
            self.doctors_tab,
            columns=('№', 'ФИО', 'Специальность'),
            show='headings'
        )
        self.doctors_table.heading('№', text='№')
        self.doctors_table.heading('ФИО', text='ФИО')
        self.doctors_table.heading('Специальность', text='Специальность')

        self.doctors_table.pack(fill=tk.BOTH, expand=True)

        self.doctor_current_page = 1
        self.doctor_page_size = 10

        button_frame = tk.Frame(self.doctors_tab)
        button_frame.pack(fill="x", pady=10)

        add_doctor_button = tk.Button(button_frame, text="Добавить доктора", command=lambda: controller.open_add_doctor_window(self.root))
        add_doctor_button.pack(side="left", pady=10)

        delete_doctor_button = tk.Button(button_frame, text="Удалить доктора", command=lambda: controller.delete_doctor(self.doctors_table))
        delete_doctor_button.pack(side="left", pady=10)

        change_doctor_button = tk.Button(button_frame, text="Скорректировать", command=lambda: controller.open_view_details_doctor_window(self.doctors_table, self.root))
        change_doctor_button.pack(side="left", pady=10)

        next_doctor_button = tk.Button(button_frame, text="Следующий", command=self.next_doctor_page)
        next_doctor_button.pack(side="right", pady=10)

        prev_doctor_button = tk.Button(button_frame, text="Предыдущий", command=self.prev_doctor_page)
        prev_doctor_button.pack(side="right", pady=10)

        self.refresh_doctors_table()

    def update(self, action, data):
        if action in ("addClient", "updateClient", "deleteClient"):
            self.refresh_clients_table()
        if action in ("addDoctor", "deleteDoctor", "updateDoctor"):
            self.refresh_doctors_table()

    def refresh_doctors_table(self):
        # Удаляем старые данные из таблицы
        for row in self.doctors_table.get_children():
            self.doctors_table.delete(row)

        # Получаем данные из модели
        doctors = self.controller.get_doctors(self.doctor_page_size, self.doctor_current_page)
        if not doctors:
            if self.controller.model.get_count_doctors() > 0:
                self.doctor_current_page -= 1
                self.refresh_doctors_table()
            print("Нет данных для отображения")
            return

        for index, doctors in enumerate(doctors, 1):
            self.doctors_table.insert(
                '',
                'end',
                values=(
                    index + (self.doctor_current_page - 1) * 10,
                    doctors['fullname'],
                    doctors['activity']
                ),
                iid=doctors['id']  # Сохраняем ID как идентификатор строки
            )
            
    def refresh_clients_table(self):
        # Удаляем старые данные из таблицы
        for row in self.client_table.get_children():
            self.client_table.delete(row)

        # Получаем данные из модели
        clients = self.controller.get_clients(self.client_page_size, self.client_current_page)
        if not clients:
            if self.controller.model.get_count() > 0:
                self.client_current_page -= 1
                self.refresh_clients_table()
            print("Нет данных для отображения")
            return

        for index, client in enumerate(clients, 1):
            self.client_table.insert(
                '',
                'end',
                values=(
                    index + (self.client_current_page - 1) * 10,
                    client['fullname'],
                    client['phone_number'],
                    client['male'],
                    client['email'],
                    client['document']
                ),
                iid=client['id']  # Сохраняем ID как идентификатор строки
            )

    def prev_client_page(self):
        if self.client_current_page > 1:
            self.client_current_page -= 1
            self.refresh_clients_table()

    def next_client_page(self):
        self.client_current_page += 1
        self.refresh_clients_table()

    def prev_doctor_page(self):
        if self.doctor_current_page > 1:
            self.doctor_current_page -= 1
            self.refresh_doctors_table()

    def next_doctor_page(self):
        self.doctor_current_page += 1
        self.refresh_doctors_table()
