from SrviceLog import ServiceLog
from AddUpdateServiceView import AddUpdateServiceView
from Client import Client
from Doctor import Doctor
import tkinter as tk
from tkinter import ttk, messagebox

class ServiceLogByClientController:
    def __init__(self, model):
        self.model = model

    def delete_service(self, table):
        selected_item = table.selection()
        if not selected_item:
            messagebox.showwarning("Ошибка", "Выберите услугу для удаления")
            return

        for row in table.get_children():
            print(row, selected_item)
            if selected_item[0] == row:
                table.delete(row)

        # Получаем ID выбранного клиента
        service_id = selected_item[0]
        self.model.delete_service(service_id)

        messagebox.showinfo("Успех", "Услуга успешно удалена!")

    def get_services(self, page_size, page_num, client):
        logs = self.model.get_services(page_size, page_num)
        newClient = Client(client.get_fullname(),client.get_phone_number(),client.get_male(), client.get_email(), client.get_age(),client.get_allergic_reactions(),client.get_document(), client.get_id())
       
        for log in logs:
            doctor_data = self.model.get_doctor_by_id(log['doctor_id'])
            doctor = Doctor(doctor_data['fullname'], doctor_data['activity'], doctor_data['qualification'], doctor_data['experience'], doctor_data['id'])
             # Преобразуем каждый лог в экземпляр ServiceLog
            service_log = ServiceLog(
                client_id=log['client_id'],
                doctor=doctor,
                name_log=log['name_log'],
                cost=log['cost'],
                diagnosis=log['diagnosis'],
                log_id=log['log_id']
            )

            # Добавляем лог в список клиента
            if log['client_id'] == newClient.get_id() and not (service_log in newClient.get_service_logs()):
                newClient.add_service_log(service_log)
                print(service_log)
        return newClient

    def open_add_service_window(self, root, client):
        new_window = tk.Toplevel(root)
        AddUpdateServiceView(new_window, "add", self.model, client)
