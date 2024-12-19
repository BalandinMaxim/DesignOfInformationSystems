import tkinter as tk
from tkinter import ttk, messagebox

class ChooseDoctorController:
    def __init__(self, model):
        self.model = model

    def get_doctors(self, page_size, page_num):
        return self.model.get_doctors(page_size, page_num)

    def choose_doctor(self, table, root, addUpdateServiceView):
        selected_item = table.selection()

        if not selected_item:
            messagebox.showwarning("Ошибка", "Выберите доктора для просмотра")
            return

        doctor_id = selected_item[0]

        if doctor_id != None:
            client_data = self.model.get_doctor_by_id(doctor_id)

            addUpdateServiceView.doctor_id_entry.configure(state="normal")  # Временно разблокировать
            addUpdateServiceView.doctor_id_entry.delete(0, tk.END)  # Очистить текущее значение
            addUpdateServiceView.doctor_id_entry.insert(0, doctor_id)  # Вставить новый текст
            addUpdateServiceView.doctor_id_entry.configure(state="readonly")  # Вернуть readonly

            addUpdateServiceView.doctor_entry.configure(state="normal")  # Временно разблокировать
            addUpdateServiceView.doctor_entry.delete(0, tk.END)  # Очистить текущее значение
            addUpdateServiceView.doctor_entry.insert(0, client_data['fullname'])  # Вставить новый текст
            addUpdateServiceView.doctor_entry.configure(state="readonly")  # Вернуть readonly

            root.destroy()
        else:
            messagebox.showwarning("Ошибка", "Не удалось найти доктора в базе данных")
