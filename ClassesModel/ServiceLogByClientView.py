from tkinter import ttk, messagebox
from ServiceLogByClientController import ServiceLogByClientController
import tkinter as tk

class ServiceLogByClientView:
    def __init__(self, root, model, client):
        self.root = root
        self.root.lift()
        self.root.grab_set()
        self.root.title("Предоставленные услуги по клиенту")
        self.controller = ServiceLogByClientController(model)
        self.controller.model.add_observer(self)
        self.model = model

        self.client = client

        self.serviceLog_table = ttk.Treeview(
            root,
            columns=('№', 'Название записи', 'Стоимость', 'Диагноз', 'Имя доктора', 'doctor_id', 'client_id'),
            show='headings'
        )
        self.serviceLog_table.heading('№', text='№')
        self.serviceLog_table.heading('Название записи', text='Название записи')
        self.serviceLog_table.heading('Стоимость', text='Стоимость')
        self.serviceLog_table.heading('Диагноз', text='Диагноз')
        self.serviceLog_table.heading('Имя доктора', text='Имя доктора')
        self.serviceLog_table.heading('doctor_id', text='doctor_id')
        self.serviceLog_table.heading('client_id', text='client_id')

        self.serviceLog_table.column('doctor_id', width=0, stretch=False)
        self.serviceLog_table.column('client_id', width=0, stretch=False)

        self.serviceLog_table.pack(fill=tk.BOTH, expand=True)

        button_frame = tk.Frame(root)
        button_frame.pack(fill="x", pady=10)

        add_doctor_button = tk.Button(button_frame, text="Добавить услугу (прием)", command=lambda: self.controller.open_add_service_window(self.root, self.client))
        add_doctor_button.pack(side="left", pady=10)

        delete_doctor_button = tk.Button(button_frame, text="Удалить услугу (прием)", command=lambda: self.controller.delete_service(self.serviceLog_table))
        delete_doctor_button.pack(side="left", pady=10)

        next_doctor_button = tk.Button(button_frame, text="Следующий", command=self.next_page)
        next_doctor_button.pack(side="right", pady=10)

        prev_doctor_button = tk.Button(button_frame, text="Предыдущий", command=self.prev_page)
        prev_doctor_button.pack(side="right", pady=10)

        self.current_page = 1
        self.page_size = 10
        self.refresh_table()

    def update(self, action, data):
        if action in ("addserviceLog", "deleteServiceLog"):
            self.refresh_table()

    def refresh_table(self):
        # Удаляем старые данные из таблицы
        try:
            if self.serviceLog_table.get_children():
                for row in self.serviceLog_table.get_children():
                    print(f"Удаляю строку с id: {row}")
                    self.serviceLog_table.delete(row)
            else:
                print("Таблица уже пуста.")
        except Exception:
            print("Ошибка обращении к таблице")

        # Получаем данные из модели
        self.client = self.controller.get_services(self.page_size, self.current_page, self.client)
        services = self.client.get_service_logs()

        if not services:
            if len(services) == 0:
                if self.current_page != 1:
                    self.current_page -= 1
                    self.refresh_table()
            print("Нет данных для отображения")
            return

        index = 1

        for service in services:
            self.serviceLog_table.insert(
                '',
                'end',
                values=(
                    index + (self.current_page - 1) * 10,
                    service.get_name_log(),
                    service.get_cost(),
                    service.get_diagnosis(),
                    service.get_doctor().get_fullname(),
                    service.get_doctor().get_doctor_id(),
                    service.get_client_id()),
                iid=service.get_log_id()  # Сохраняем ID как идентификатор строки
            )

    def prev_page(self):
        if self.current_page > 1:
            self.current_page -= 1
            self.refresh_table()

    def next_page(self):
        self.current_page += 1
        self.refresh_table()
