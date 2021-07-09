class Transaction:
    def __init__(
            self, wallet_receiver,
            wallet_emitter, mount):
        self._wallet_receiver = wallet_receiver
        self._wallet_emitter = wallet_emitter
        self._mount = mount

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_wallet_receiver(self):
        return self._wallet_receiver

    def get_wallet_emitter(self):
        return self._wallet_emitter

    def get_mount(self):
        return self._mount