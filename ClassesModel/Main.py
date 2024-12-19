from Client_rep_DB import ClientRepDB
from FasadModel import FasadModel
from MainView import MainView
from MainController import MainController
from DatabaseConnection import DatabaseConnection
from Doctor_rep_DB import DoctorRepDB
from ServiseLog_rep_DB import ServiceLogRepDB
import tkinter as tk

if __name__ == "__main__":
    # Подключение к базе данных
    db_config = {
        'dbname': "DiagramClasses",
        'user': "postgres",
        'password': "maxim16",
        'host': "localhost",
        'port': 5432
    }

    # Создание репозитория и модели
    db_connection = DatabaseConnection(db_config)
    repositoryClient = ClientRepDB(db_connection)
    repositoryDoctor = DoctorRepDB(db_connection)
    repositoryService = ServiceLogRepDB(db_connection)

    model = FasadModel(repositoryClient, repositoryDoctor, repositoryService)

    # Создание и запуск главного окна
    root = tk.Tk()
    main_controller = MainController(model)
    MainView(root, main_controller)
    root.mainloop()

