class Transaction:
    def __init__(
            self, wallet_transmitter,
            wallet_emitter, price_number):
        self._wallet_transmitter = wallet_transmitter
        self._wallet_emitter = wallet_emitter
        self._price_number = price_number

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_wallet_transmitter(self):
        return self._wallet_transmitter

    def get_wallet_emitter(self):
        return self._wallet_emitter

    def get_price_number(self):
        return self._price_number