import logging
import tkinter as tk
import tkinter.scrolledtext as ScrolledText


class TextHandler(logging.Handler):
    def __init__(self, text):
        # run the regular Handler __init__
        logging.Handler.__init__(self)
        # Store a reference to the Text it will log to
        self.text = text

    def emit(self, record):
        msg = self.format(record)
        def append():
            self.text.configure(state='normal')
            self.text.insert(tk.END, msg + '\n')
            self.text.configure(state='disabled')
            # Autoscroll to the bottom
            self.text.yview(tk.END)
        # This is necessary because we can't modify the Text from other threads
        self.text.after(0, append)

class MarketGUI(tk.Frame):
    def __init__(self, parent, title, log_name, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.title = title
        self.log_name = log_name

    def build(self):
        # Build GUI
        self.root.title(self.title)
        self.root.option_add('*tearOff', 'FALSE')
        self.grid(column=0, row=0, sticky='ew')
        self.grid_columnconfigure(0, weight=1, uniform='a')
        self.grid_columnconfigure(1, weight=1, uniform='a')
        self.grid_columnconfigure(2, weight=1, uniform='a')
        self.grid_columnconfigure(3, weight=1, uniform='a')

        # Add text widget to display logging info
        st = ScrolledText.ScrolledText(self, state='disabled')
        st.configure(font='TkFixedFont')
        st.grid(column=0, row=1, sticky='w', columnspan=4)

        # Create textLogger
        text_handler = TextHandler(st)

        # Logging configuration
        logging.basicConfig(filename=self.log_name,
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s')

        # Add the handler to logger
        logger = logging.getLogger()
        logger.addHandler(text_handler)
