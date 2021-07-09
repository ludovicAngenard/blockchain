from classes.settings.settings import MAX_TOKEN_NUMBER
from classes.Wallet import *
from classes.Chain import *

wallet1 = Wallet(MAX_TOKEN_NUMBER)
wallet2 = Wallet(MAX_TOKEN_NUMBER)

chain = Chain()

for i in range(10*2**32): ## create multiple transaction to test the files generation
    chain.add_transaction(Transaction(wallet1,wallet2, 50))