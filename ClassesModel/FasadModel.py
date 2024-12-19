class Observable:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, action, data):
        for observer in self._observers:
            observer.update(action, data)

class FasadModel(Observable):
    def __init__(self, repositoryClient, repositoryDoctor, repositoryService):
        super().__init__()
        self._repositoryClient = repositoryClient
        self._repositoryDoctor = repositoryDoctor
        self._repositoryService = repositoryService

    def get_clients(self, page_size, page_num):
        offset = (page_num - 1) * page_size
        return self._repositoryClient.get_k_n_short_list(page_size, offset)

    def get_client_by_id(self, client_id):
        return self._repositoryClient.get_by_id(client_id)

    def add_client(self, client):
        client_id = self._repositoryClient.add(client)
        self.notify_observers("addClient", {"id": client_id})

    def update_client(self, client):
        self._repositoryClient.update_by_id(client)
        self.notify_observers("updateClient", {"id": client.get_id()})

    def delete_client(self, client_id):
        self._repositoryClient.delete_by_id(client_id)
        self.notify_observers("deleteClient", {"id": client_id})

    def get_count(self):
        return self._repositoryClient.get_count()

    def get_doctors(self, page_size, page_num):
        offset = (page_num - 1) * page_size
        return self._repositoryDoctor.get_k_n_short_list(page_size, offset)

    def add_doctor(self, doctor):
        doctor_id = self._repositoryDoctor.add(doctor)
        self.notify_observers("addDoctor", {"id": doctor_id})

    def get_count_doctors(self):
        return self._repositoryDoctor.get_count()

    def delete_doctor(self, doctor_id):
        self._repositoryDoctor.delete_by_id(doctor_id)
        self.notify_observers("deleteDoctor", {"id": doctor_id})

    def get_doctor_by_id(self, doctor_id):
        return self._repositoryDoctor.get_by_id(doctor_id)

    def update_doctor(self, doctor):
        self._repositoryDoctor.update_by_id(doctor)
        self.notify_observers("updateDoctor", {"id": doctor.get_doctor_id()})

    def get_services(self, page_size, page_num):
        offset = (page_num - 1) * page_size
        return self._repositoryService.get_k_n_short_list(page_size, offset)

    def get_count_services(self):
        return self._repositoryService.get_count()

    def add_service(self, serviceLog):
        serviceLog_id = self._repositoryService.add(serviceLog)
        self.notify_observers("addserviceLog", {"id": serviceLog_id})

    def delete_service(self, service_id):
        self._repositoryService.delete_by_id(service_id)
        self.notify_observers("deleteServiceLog", {"id": service_id})
