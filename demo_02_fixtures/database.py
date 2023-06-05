class Database:
    def __init__(self):
        self._data = {}

    def insert_data(self, key, value):
        self._data[key] = value

    def get_data(self, key):
        return self._data.get(key)


db = Database()

db.insert_data('key','val')
print(db.get_data('key'))