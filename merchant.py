from entity import Entity
import time
import logging

class Merchant(Entity):
    def __init__(self):
        super().__init__()
        super().start(self.buy)
        super().start(self.sell)
        super().start(self.kill)

    def buy(self):
        while True:
            # Report time / date at 2-second intervals
            time.sleep(1)
            timeStr = time.asctime()
            msg = "BUY"
            logging.info(msg)

    def sell(self):
        while True:
            # Report time / date at 2-second intervals
            time.sleep(1)
            timeStr = time.asctime()
            msg = "SELL"
            logging.info(msg)

    def kill(self):
        time.sleep(10)
        self.stop(self.buy.__name__)