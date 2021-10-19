import gui
import time
import tkinter as tk
import threading
import logging
import merchant

def main():

    root = tk.Tk()
    main_window = gui.MarketGUI(root, "Main Window", "Main_Window.log")
    main_window.build()

    merchant.Merchant()

    root.mainloop()


if __name__ == "__main__":
    main()