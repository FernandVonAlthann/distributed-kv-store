class KeyValueStore:
    def __init__(self):
        self.store = {}

    def put(self, key, value):
        self.store[key] = value
        return "OK"

    def get(self, key):
        return self.store.get(key, "")

    def delete(self, key):
        if key in self.store:
            del self.store[key]
            return "OK"
        return "NotFound"
