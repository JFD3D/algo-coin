
from algo_coin.util.util import *
from algo_coin.connectivity.coinbase import *
from abc import abstractmethod


class Wallet(Endpoint):
    def __init__(self, type):
        """ """
        super().__init__(type)

    def APIInit(self, api_key):
        """ """
        if self.type is ExchangeType.coinbase:
            self.wallet_api = CoinbaseWalletAPI(api_key)
        return self.wallet_api.APIInit()

    @abstractmethod
    def deposit(self, source):
        """ """
        pass

    @abstractmethod
    def withdraw(self, destination):
        """ """
        pass
