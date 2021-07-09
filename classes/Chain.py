import hashlib
import os
from classes.Block import *
from classes.Transaction import *
class Chain:
    last_transaction_number = 0

    def __init__(
            self, blocks = []):
        self.blocks = blocks
        new_block = Block('00', '00')
        self.blocks.append(new_block)
        new_block.save()

    def generate_hash(self):
        hash = self.create_hashe()
        return hash

    def create_hashe(self):
        number = 0
        number_string = str(number)
        number_hashed = hashlib.sha256(number_string.encode()).hexdigest()
        print('search a good hash')
        while not self.verify_hash(number_hashed):
            number += 1
            number_string = str(number)
            number_hashed = hashlib.sha256(number_string.encode()).hexdigest()
        return number_hashed

    def verify_hash(self, hash):
        if hash[0:4] == '0000':
            for block in self.blocks:
                if block.get_hash() == hash:
                    return False
            return True


    def formalize(self):
        pass

    def add_block(self, hash):
        new_block = Block(hash, self.blocks[-1].get_hash())
        self.blocks.append(new_block)
        print('create a block')
        new_block.save()

    def get_block(self, hash):
        for block in self.blocks:
            if block.get_hash() == hash:
                return block

    def add_transaction(self, transaction: Transaction):
        if (not transaction.get_wallet_emitter() and not transaction.get_wallet_receiver() and not self.verify_balance(transaction)):
            return False
        else:
            if not self.verify_weight(transaction):
                self.add_block(self.generate_hash())
            else:
                Chain.last_transaction_number += 1
                transaction.set_id(Chain.last_transaction_number)
                self.blocks[-1].add_transaction(transaction)

    def verify_balance(self, transaction:Transaction):
        if transaction.get_wallet_emitter().get_balance() >= transaction.get_mount():
            return True
        else:
            return False

    def verify_weight(self, transaction):
        transaction_bytes = len(str(transaction).encode('utf-8'))
        max_bytes = 256000
        last_block_space = max_bytes - self.blocks[-1].get_weight()
        if last_block_space >= transaction_bytes:
            return True
        else:
            return False

    @staticmethod
    def get_last_transaction_number():
        return Chain.last_transaction_number
