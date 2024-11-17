class ClientRepFileAdapter:

    def __init__(self, client_rep_file: ClientRepFile):
        client_rep_file.read_data_from_file()
        self._client_rep_file = client_rep_file

    def get_k_n_short_list(self, k, n):
        return self._client_rep_file.get_k_n_short_list(k, n)

    def get_by_id(self, id):
        return self._client_rep_file.get_by_id(id)

    def delete_by_id(self, id):
        self._client_rep_file.delete_by_id(id)
        self._client_rep_file.write_data_to_file()

    def update_by_id(self, entity_id, fullname, phone_number, male, email, age, allergic_reactions, document):
        self._client_rep_file.replace_by_id(entity_id, fullname, phone_number, male, email, age, allergic_reactions, document)
        self._client_rep_file.write_data_to_file()

    def add(self, fullname, phone_number, male, email, age, allergic_reactions, document):
        self._client_rep_file.add_entity(fullname, phone_number, male, email, age, allergic_reactions, document)
        self._client_rep_file.write_data_to_file()

    def get_count(self):
        return self._client_rep_file.get_count()
