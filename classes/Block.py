class Block:

    def __init__(self, unique_id, hash, parent_hash, transactions):
        self.unique_id = unique_id
        self.hash = hash
        self.parent_hash = parent_hash
        self.transactions = transactions

    def check_hash(self):
        pass

    def add_transaction(self):
        pass

    def get_transaction(self):
        pass

    def get_weight(self):
        pass

    def save(self):
        pass

    def load(self):
        pass
