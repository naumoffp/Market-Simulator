import threading

class Entity():
    def __init__(self):
        self.tag = None
        self.threads = {}

        # Tag ID onto new existence

    @staticmethod
    def _thread_runtime_factory(thread_object):
        def thread_runtime(function):
            def validate_thread(*args, **kwargs):
                # self is always the first argument
                self = args[0]
                if self.threads[thread_object] == True:
                    function(*args, **kwargs)

            return validate_thread

        return thread_runtime



    def make_tag(self):
        return True

    def start(self, function, *args, **kwargs):
        thread = threading.Thread(target=function, args=[*args], kwargs={**kwargs})
        self.add_thread(thread)
        return thread

        # Fix RuntimeError: main thread is not in main loop
        thread.daemon = True
        thread.start()

    def stop(self, name):
        print("Killing: " + str(self.threads[name]))
        self.threads[name].join()

    def add_thread(self, thread_object):
        # Format: {Thread Object: Is Running}
        strict_format = {thread_object: True}
        self.threads.update(strict_format)



