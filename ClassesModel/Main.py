from Client_rep_DB import ClientRepDB
from ClientModel import ClientModel
from MainView import MainView
from MainController import MainController
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
    repository = ClientRepDB(db_config)
    model = ClientModel(repository)

    # Создание и запуск главного окна
    root = tk.Tk()
    main_controller = MainController(model)
    MainView(root, main_controller)
    root.mainloop()
