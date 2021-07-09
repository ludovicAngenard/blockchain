import uuid
import json

class Wallet:
    def __init__(
            self, unique_id,
            balance, history):
        self._unique_id = unique_id
        self._balance = balance
        self._history = history

    def generate_unique_id(self):
        uuid = uuid.uuid4()
        for wallet in self.load():
            if wallet.unique_id == self.get_unique_id():
                self.generate_unique_id()
        return uuid

    def add_balance(self, balance):
        self.set_balance(
            self.get_balance() + balance
            )

    def sub_balance(self, balance):
        self.set_balance(
            self.get_balance() - balance
            )

    def send(self):
        pass

    def save(self):
        with open("./content/wallets/{}.json".format(self.get_unique_id()), 'w') as f:
            data = {
                "unique_id": self.get_unique_id(),
                "balance": self.get_balance(),
                "history": self.get_history()
            }
            json.dump(data, f)


    def load(self):
        with open("./content/wallets/{}.json".format(self.get_unique_id())) as f:
            data = json.load(f)
        return data

    def get_unique_id(self):
        return  self._unique_id

    def get_balance(self):
        return self._balance

    def get_history(self):
        return self._history

    def set_balance(self, balance):
        self._balance = balance

    def set_history(self, history):
        self._history = history