
class Row:

    def __init__(self, value, inserted_id):
        self.value = value
        self.inserted_id = inserted_id
        pass

    def __str__(self):
        return str(self.inserted_id) + ' -> ' + str(self.value)


class Collection:

    def __init__(self):
        self.data = {}
        self.counter = 0
        pass

    def delete_many(self, param):
        for item in param:
            self.data.pop(item)
        pass

    def insert_one(self, param):
        self.counter = 1 + self.counter
        self.data[self.counter] = Row(param, self.counter)
        return self.data[self.counter]

    def print_all(self):
        for item in self.data:
            print(self.data[item])

    def get_all_rows(self):
        return self.data


class Mongo:
    def __init__(self):
        self.collection_names = []
        self.collection_dict = {}
        pass

    def list_collection_names(self):
        return self.collection_names

    def create_collection(self, param):
        self.collection_names.append(param)
        self.collection_dict[param] = Collection()
        setattr(self, param, self.collection_dict[param])
        pass

    def get_all_collections(self):
        return self.collection_dict

