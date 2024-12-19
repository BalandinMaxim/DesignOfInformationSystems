import tkinter as tk
from tkinter import ttk
from ChooseDoctorController import ChooseDoctorController

class ChooseDoctorView:
    def __init__(self, addUpdateServiceView, root, model):
        self.model = model
        self.controller = ChooseDoctorController(model)
        self.root = root
        self.addUpdateServiceView = addUpdateServiceView

        self.doctors_table = ttk.Treeview(
            root,
            columns=('№', 'ФИО', 'Специальность'),
            show='headings'
        )
        self.doctors_table.heading('№', text='№')
        self.doctors_table.heading('ФИО', text='ФИО')
        self.doctors_table.heading('Специальность', text='Специальность')

        self.doctors_table.pack(fill=tk.BOTH, expand=True)

        self.doctor_current_page = 1
        self.doctor_page_size = 10

        button_frame = tk.Frame(self.root)
        button_frame.pack(fill="x", pady=10)

        add_doctor_button = tk.Button(button_frame, text="Выбрать доктора", command=lambda: self.controller.choose_doctor(self.doctors_table, self.root, self.addUpdateServiceView))
        add_doctor_button.pack(side="left", pady=10)

        next_doctor_button = tk.Button(button_frame, text="Следующий", command=self.next_doctor_page)
        next_doctor_button.pack(side="right", pady=10)

        prev_doctor_button = tk.Button(button_frame, text="Предыдущий", command=self.prev_doctor_page)
        prev_doctor_button.pack(side="right", pady=10)

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

    def prev_doctor_page(self):
        if self.doctor_current_page > 1:
            self.doctor_current_page -= 1
            self.refresh_doctors_table()

    def next_doctor_page(self):
        self.doctor_current_page += 1
        self.refresh_doctors_table()
