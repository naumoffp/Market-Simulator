import threading
import uuid

class Base():
    def __init__(self):
        self.tag = None

        # Tag ID onto new existence
        self.make_tag()

    @staticmethod
    def threaded(function):
        def wrapper(*args, **kwargs):
            thread = threading.Thread(target=function, args=args, kwargs=kwargs)
            # Fix TK RuntimeError: main thread is not in main loop
            thread.daemon = True
            thread.start()
            return thread

        return wrapper

    def make_tag(self):
        self.tag = uuid.uuid4()

