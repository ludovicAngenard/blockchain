import json
import os
class Block:

    def __init__(
            self, hash, parent_hash,
            base_hash = 64):
        self._hash = hash
        self._parent_hash = parent_hash
        self._base_hash = base_hash
        self.transactions = []

    def check_hash(self):
        character_number = 0
        for i in self._get_hash():
            character_number += 1
        if character_number == self._get_base_hash():
            return True
        else:
            return False

    def add_transaction(self, transaction):
        self.transactions.append(str(transaction))
        self.save()

    def get_transaction(self, transaction_number):
        for transaction in self.transactions():
            if transaction.get_id() == transaction:
                return transaction
        return False

    def get_weight(self):
        weight = os.path.getsize("classes/content/blocs/{}.json".format(self.get_hash()))
        return weight

    def save(self):
        with open("classes/content/blocs/{}.json".format(self.get_hash()), 'w+') as f:
            data = {
                "hash": self.get_hash(),
                "base_hash": self.get_base_hash(),
                "parent_hash": self.get_parent_hash(),
                "transactions": self.transactions,
            }
            json.dump(data, f)

    def load(self):
        with open("classes/content/blocs/{}.json".format(self.get_hash())) as f:
            data = json.load(f)
        return data

    def get_hash(self):
        return self._hash

    def get_parent_hash(self):
        return self._parent_hash

    def set_parent_hash(self, parent_hash):
        self._parent_hash = parent_hash

    def get_base_hash(self):
        return self._base_hash

    def set_base_hash(self, base_hash):
        self._base_hash = base_hash
