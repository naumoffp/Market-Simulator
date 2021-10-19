import entity
import time
import logging

class Merchant(entity.Base):
    def __init__(self):
        super().__init__()

    @entity.Base.threaded
    def buy(self):
        while True:
            # Report time / date at 2-second intervals
            time.sleep(1)
            timeStr = time.asctime()
            msg = "BUY"
            logging.info(msg)

    @entity.Base.threaded
    def sell(self):
        while True:
            # Report time / date at 2-second intervals
            time.sleep(1)
            timeStr = time.asctime()
            msg = "SELL"
            logging.info(msg)