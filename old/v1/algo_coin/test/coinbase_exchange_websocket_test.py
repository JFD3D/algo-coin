
from autobahn.twisted.websocket import WebSocketClientFactory,  \
    WebSocketClientProtocol, connectWS
from twisted.python import log
from twisted.internet import reactor
#from pprint import pprint
import sys
import json


class CoinbaseExchangeClientProtocol(WebSocketClientProtocol):

    def onOpen(self):
        msg = json.dumps({"type": "subscribe", "product_id": "BTC-USD"})
        res = self.sendMessage(msg.encode('utf-8'), isBinary=False)
        print(res)

    def onMessage(self, payload, isBinary):
        if not isBinary:
            msg = json.loads(payload.decode('utf8'))
            print(msg)
            #pprint(msg)

if __name__ == '__main__':

    log.startLogging(sys.stdout)
    factory = WebSocketClientFactory("wss://ws-feed.exchange.coinbase.com",
                                     debug=True)
    factory.protocol = CoinbaseExchangeClientProtocol
    connectWS(factory)
    reactor.run()
