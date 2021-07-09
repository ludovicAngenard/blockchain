import hashlib
import os
from Block import Block
from Transaction import Transaction

class Chain:
    last_transaction_number = 0

    def __init__(
            self, blocks):
        self.blocks = blocks
        self.first_block()

    def generate_hash(self):
        hash = self.create_hashe()
        return hash

    def create_hashe(self):
        number = 0
        number_string = str(number)
        number_hashed = hashlib.sha256(number_string.encode()).hexdigest()
        while self.verify_hash(number_hashed) == False:
            print('non')
            number_string = str(number)
            number_hashed = hashlib.sha256(number_string.encode()).hexdigest()
        return number_hashed

    def verify_hash(self, hash):
        if hash[0:4] == '0000':
            for block in blocks:
                print(block.get_hashe(), 'oui')
                if block.get_hashe() == hash:
                    return False
            return True


    def formalize(self):
        pass

    def add_block(self, hash):
        if len(self.blocks) > 0:
            new_block = Block(hash, self.blocks[-1])
        else:
            new_block = Block(hash, None)
        self.blocks.append(new_block)
        new_block.save()

    def get_block(self, hash):
        for block in self.blocks:
            if block.get_hash() == hash:
                return block

    def add_transaction(self, block: Block, transaction: Transaction):
        if (not transaction.get_wallet_emitter()
                and not transaction.get_wallet_transmitter()
                and not self.verify_balance(transaction)):
            return False
        else:
            if not self.verify_weight(transaction):
                self.add_block(self.generate_hash())
            else:
                last_transaction_number += 1
                transaction.set_id(last_transaction_number)
                block.add_transaction(transaction)

    def verify_balance(self, transaction:Transaction):
        if transaction.get_wallet_emitter().get_balance() >= transaction.get_price_number():
            return True
        else:
            return False

    def verify_weight(self, transaction):
        transaction_bytes = bytes(str(transaction), 'utf-8')
        max_bytes = 256000
        last_block_space = max_bytes - self.blocks[-1].get_weight()
        if last_block_space >= transaction_bytes:
            return True
        else:
            return False

    def first_block(self):
        first_one = Block('00', '00')
        self.blocks.append(first_one)

    @staticmethod
    def get_last_transaction_number():
        return last_transaction_number
