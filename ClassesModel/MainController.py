import tkinter as tk
from AddUpdateClientController import AddUpdateClientController
from AddUpdateClientView import AddUpdateClientView
from ServiceLogByClientView import ServiceLogByClientView
from Client import Client
from tkinter import ttk, messagebox

from AddUpdateDoctorView import AddUpdateDoctorView

class MainController:

    def __init__(self, model):
        self.model = model

    def get_clients(self, page_size, page_num):
        return self.model.get_clients(page_size, page_num)

    def get_doctors(self, page_size, page_num):
        return self.model.get_doctors(page_size, page_num)

    def open_add_client_window(self, controller, root):
        new_window = tk.Toplevel(root)
        addController = AddUpdateClientController(controller.model)
        AddUpdateClientView(new_window, addController, "add")

    def view_details(self, table, root, controller):
        selected_item = table.selection()

        if not selected_item:
            messagebox.showwarning("Ошибка", "Выберите клиента для просмотра")
            return

        client_id = selected_item[0]

        if client_id != None:
            new_window = tk.Toplevel(root)
            addController = AddUpdateClientController(controller.model)
            AddUpdateClientView(new_window, addController, "update", client_id)
        else:
            messagebox.showwarning("Ошибка", "Не удалось найти клиента в базе данных")

    def delete_client(self, table):
        selected_item = table.selection()
        if not selected_item:
            messagebox.showwarning("Ошибка", "Выберите клиента для удаления")
            return

        # Получаем ID выбранного клиента
        client_id = selected_item[0]
        self.model.delete_client(client_id)
        messagebox.showinfo("Успех", "Клиент успешно удален!")

    def open_add_doctor_window(self, root):
        new_window = tk.Toplevel(root)
        AddUpdateDoctorView(new_window, "add", self.model)

    def delete_doctor(self, table):
        selected_item = table.selection()
        if not selected_item:
            messagebox.showwarning("Ошибка", "Выберите доктора для удаления")
            return

        # Получаем ID выбранного клиента
        doctor_id = selected_item[0]
        self.model.delete_doctor(doctor_id)
        messagebox.showinfo("Успех", "Доктор успешно удален!")

    def open_view_details_doctor_window(self, table, root):
        selected_item = table.selection()

        if not selected_item:
            messagebox.showwarning("Ошибка", "Выберите доктора для просмотра")
            return

        doctor_id = selected_item[0]

        if doctor_id != None:
            new_window = tk.Toplevel(root)
            AddUpdateDoctorView(new_window, "update", self.model, doctor_id)
        else:
            messagebox.showwarning("Ошибка", "Не удалось найти доктора в базе данных")

    def showServiceLogs_details(self, table, root):
        selected_item = table.selection()

        if not selected_item:
            messagebox.showwarning("Ошибка", "Выберите клиента для просмотра")
            return

        client_id = selected_item[0]

        if client_id != None:
            new_window = tk.Toplevel(root)
            client_data = self.model.get_client_by_id(client_id)
            client = Client(client_data['fullname'], client_data['phone_number'], client_data['male'],client_data['email'],
                            client_data['age'], client_data['allergic_reactions'],  client_data['document'], client_data['id'])
            ServiceLogByClientView(new_window, self.model, client)
        else:
            messagebox.showwarning("Ошибка", "Не удалось найти клиента в базе данных")
