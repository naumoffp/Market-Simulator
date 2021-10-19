import threading

class Entity():
    def __init__(self):
        self.tag = None
        self.threads = {}

        # Tag ID onto new existence

    def make_tag(self):
        return True

    def start(self, function, *args, **kwargs):
        name = function.__name__
        thread = threading.Thread(target=self.worker, args=[name, function, *args], kwargs={**kwargs})
        self.add_thread(function.__name__, thread)

        # Fix RuntimeError: main thread is not in main loop
        thread.daemon = True
        thread.start()

    def stop(self, name):
        self.threads[name][1] = False
        return True

    def worker(self, name, function, *args, **kwargs):
        while(self.verify_thread(name)):
            function(*args, **kwargs)

    def add_thread(self, name, thread):
        # Format: {Name: [Thread Object, Is Running]}
        strict_format = {name: [thread, True]}
        self.threads.update(strict_format)
        return True

    def verify_thread(self, name):
        thread_info = self.threads[name]

        if thread_info[1]:
            return True

        return False



