import tkinter as tk
from tkinter import messagebox
from ChooseDoctorView import ChooseDoctorView
from AddServiceController import AddServiceController

class AddUpdateServiceView:
    def __init__(self, root, action, model, client=None):
        self.action = action
        self.client = client
        self.root = root

        # Поля ввода данных
        tk.Label(root, text="Название услуги").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.name_log_entry = tk.Entry(root, width=30)
        self.name_log_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Стоимость").grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.cost_entry = tk.Entry(root, width=30)
        self.cost_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Поставленный диагноз").grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.diagnosis_entry = tk.Entry(root, width=30)
        self.diagnosis_entry.grid(row=2, column=1, padx=10, pady=5)

        self.doctor_label = tk.Label(root, text="Доктор").grid(row=3, column=0, sticky="w", padx=10, pady=5)
        self.doctor_entry = tk.Entry(root, width=30)
        self.doctor_entry.grid(row=3, column=1, padx=10, pady=5)
        self.doctor_entry.configure(state="readonly")

        self.doctor_id_label = tk.Label(root, text="Doctor_id")
        self.doctor_id_entry = tk.Entry(root, width=30)

        self.doctor_id_label.grid(row=3, column=0, sticky="w", padx=10, pady=5)
        self.doctor_id_entry.grid(row=3, column=1, padx=10, pady=5)

        self.doctor_id_label.grid_remove()
        self.doctor_id_entry.grid_remove()

        button_frame = tk.Frame(self.root)
        button_frame.grid(pady=10, sticky="nsew")
        #button_frame.pack(fill="x", pady=10)

        if action == "add":
            self.controller = AddServiceController(model)
            self.root.title("Добавить услугу")
            tk.Button(button_frame, text="Добавить", command=self.add_update_service).grid(row=7, column=4, columnspan=2, pady=10)

        tk.Button(button_frame, text="Подобрать доктора", command=self.choose_doctor).grid(row=7, column=8, columnspan=2, pady=10)

    def add_update_service(self):
        try:
            # Получаем данные из полей ввода
            name_log = self.name_log_entry.get().strip()
            cost = int(self.cost_entry.get().strip()) if self.cost_entry.get().strip().isdigit() else 0
            diagnosis = self.diagnosis_entry.get().strip()
            doctor_id = self.doctor_id_entry.get().strip()
            doctor_name = self.doctor_entry.get().strip()
            client_id = self.client.get_id()

        # Вызываем метод контроллера для добавления клиента
            if self.action == "add":
                self.controller.add_service(
                    name_log=name_log,
                    cost=cost,
                    diagnosis=diagnosis,
                    doctor_id=doctor_id,
                    client_id=client_id,
                    doctor_name=doctor_name
                )
                messagebox.showinfo("Успех", "Услуга успешно добавлена!")
                self.root.destroy()
      
        except ValueError as e:
            # Показываем ошибки валидации
            messagebox.showerror("Ошибка", str(e))

    def choose_doctor(self):
        new_window = tk.Toplevel(self.root)
        ChooseDoctorView(self, new_window, self.controller.model)
