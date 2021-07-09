class Transaction:
    def __init__(
            self, wallet_transmitter,
            wallet_emitter, price_number):
        self.wallet_transmitter = wallet_transmitter
        self.wallet_emitter = wallet_emitter
        self.price_number = price_number

    def get_wallet_transmitter(self):
        return self.wallet_transmitter

    def get_wallet_emitter(self):
        return self.wallet_emitter

    def get_price_number(self):
        return self.price_number