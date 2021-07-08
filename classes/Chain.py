import hashlib as hashlib

class Chain:
    last_transaction_number = 0

    def __init__(self, blocs, last_transaction_number):
        self.blocs = blocs
        self.last_transaction_number = last_transaction_number

    def generate_hash(self):
        pass

    def verify_hash(self):
        pass

    def formalize(self):
        pass

    def add_block(self):
        pass

    def get_block(self):
        pass

    def add_transaction(self):
        pass

    def first_block(self):
        pass

    def is_receiver_exist(self):
        pass

    def is_transmitter_extist(self):
        pass

    def verify_transmitter_balance(self):
        pass

    def verify_weight(self):
        pass

    def verify_block_changes(self):
        pass

    def find_transaction(self):
        pass

    def get_last_transaction_number(self):
        pass