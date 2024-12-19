import tkinter as tk
from tkinter import messagebox

class AddUpdateClientView:

    def __init__(self, root, controller, action, client_id=None):
        self.controller = controller
        self.action = action
        self.client_id = client_id
        self.root = root

        # Поля ввода данных
        tk.Label(root, text="ФИО").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.fullname_entry = tk.Entry(root, width=30)
        self.fullname_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Телефон").grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.phone_entry = tk.Entry(root, width=30)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Пол (М/Ж)").grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.male_entry = tk.Entry(root, width=30)
        self.male_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(root, text="Email").grid(row=3, column=0, sticky="w", padx=10, pady=5)
        self.email_entry = tk.Entry(root, width=30)
        self.email_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(root, text="Документ").grid(row=4, column=0, sticky="w", padx=10, pady=5)
        self.document_entry = tk.Entry(root, width=30)
        self.document_entry.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(root, text="Возраст").grid(row=5, column=0, sticky="w", padx=10, pady=5)
        self.age_entry = tk.Entry(root, width=30)
        self.age_entry.grid(row=5, column=1, padx=10, pady=5)

        tk.Label(root, text="Аллергические реакции").grid(row=6, column=0, sticky="w", padx=10, pady=5)
        self.allergic_entry = tk.Entry(root, width=30)
        self.allergic_entry.grid(row=6, column=1, padx=10, pady=5)

        if action == "add":
            self.root.title("Добавить клиента")
            tk.Button(root, text="Добавить", command=self.add_update_client).grid(row=7, column=0, columnspan=2, pady=10)
        else:
            if action == "update":

                client_data = self.controller.get_client_by_id(self.client_id)

                if client_data != None:
                    self.fullname_entry.insert(0, client_data['fullname'])
                    self.phone_entry.insert(0, client_data['phone_number'])
                    self.male_entry.insert(0, client_data['male'])
                    self.email_entry.insert(0, client_data['email'])
                    self.document_entry.insert(0, client_data['document'])
                    self.age_entry.insert(0, client_data['age'])
                    self.allergic_entry.insert(0, client_data['allergic_reactions'])

                self.root.title("Редактирование клиента")
                tk.Button(root, text="Сохранить изменения", command=self.add_update_client).grid(row=7, column=0, columnspan=2, pady=10)

    def add_update_client(self):
        try:
            # Получаем данные из полей ввода
            fullname = self.fullname_entry.get().strip()
            phone_number = self.phone_entry.get().strip()
            male = self.male_entry.get().strip().upper()
            email = self.email_entry.get().strip()
            document = self.document_entry.get().strip()
            age = int(self.age_entry.get().strip()) if self.age_entry.get().strip().isdigit() else 0
            allergic_reactions = self.allergic_entry.get().strip()

            # Вызываем метод контроллера для добавления клиента
            if self.action == "add":
                self.controller.add_client(
                    fullname=fullname,
                    phone_number=phone_number,
                    male=male,
                    email=email,
                    document=document,
                    age=age,
                    allergic_reactions=allergic_reactions
                )
                messagebox.showinfo("Успех", "Клиент успешно добавлен!")
            else:
                if self.action == "update":
                    self.controller.update_client(
                        self.client_id,
                        fullname=fullname,
                        phone_number=phone_number,
                        male=male,
                        email=email,
                        document=document,
                        age=age,
                        allergic_reactions=allergic_reactions
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
