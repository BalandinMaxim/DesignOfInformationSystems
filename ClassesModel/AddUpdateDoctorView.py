import tkinter as tk
from tkinter import messagebox
from AddDoctorController import AddDoctorController
from UpdateDoctorController import UpdateDoctorController

class AddUpdateDoctorView:
    def __init__(self, root, action, model, doctor_id=None):
       if action == "add":
            self.controller = AddDoctorController(model)
        else:
            if action == "update":
                self.controller = UpdateDoctorController(model)

        self.action = action
        self.doctor_id = doctor_id
        self.root = root

        # Поля ввода данных
        tk.Label(root, text="ФИО").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.fullname_entry = tk.Entry(root, width=30)
        self.fullname_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Специальность").grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.activity_entry = tk.Entry(root, width=30)
        self.activity_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Квалификация").grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.qualification_entry = tk.Entry(root, width=30)
        self.qualification_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(root, text="Опыт, лет").grid(row=3, column=0, sticky="w", padx=10, pady=5)
        self.experience_entry = tk.Entry(root, width=30)
        self.experience_entry.grid(row=3, column=1, padx=10, pady=5)

        if action == "add":
            self.root.title("Добавить клиента")
            tk.Button(root, text="Добавить", command=self.add_update_doctor).grid(row=7, column=0, columnspan=2, pady=10)
        else:
            if action == "update":

                client_data = self.controller.get_doctor_by_id(self.doctor_id)

                if client_data != None:
                    self.fullname_entry.insert(0, client_data['fullname'])
                    self.activity_entry.insert(0, client_data['activity'])
                    self.qualification_entry.insert(0, client_data['qualification'])
                    self.experience_entry.insert(0, client_data['experience'])

                self.root.title("Редактирование клиента")
                tk.Button(root, text="Сохранить изменения", command=self.add_update_doctor).grid(row=7, column=0, columnspan=2, pady=10)

    def add_update_doctor(self):
        try:
            # Получаем данные из полей ввода
            fullname = self.fullname_entry.get().strip()
            activity = self.activity_entry.get().strip()
            qualification = self.qualification_entry.get().strip().upper()
            experience = int(self.experience_entry.get().strip()) if self.experience_entry.get().strip().isdigit() else 0

            # Вызываем метод контроллера для добавления клиента
            if self.action == "add":
                self.controller.add_doctor(
                    fullname=fullname,
                    activity=activity,
                    qualification=qualification,
                    experience=experience
                )
                messagebox.showinfo("Успех", "Доктор успешно добавлен!")
            else:
                if self.action == "update":
                    self.controller.update_doctor(
                        self.doctor_id,
                        fullname=fullname,
                        activity=activity,
                        qualification=qualification,
                        experience=experience
                    )
                    messagebox.showinfo("Успех", "Данные клиента успешно обновлены!")

            # Уведомляем пользователя об успешном добавлении / изменении
            self.root.destroy()

        except ValueError as e:
            # Показываем ошибки валидации
            messagebox.showerror("Ошибка", str(e))
        except Exception as e:
            # Обработка других ошибок
            messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")
