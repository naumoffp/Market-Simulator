import gui
import tkinter as tk
import individual
import time


def main():

    root = tk.Tk()
    main_window = gui.MarketGUI(root, "Main Window", "Main_Window.log")
    main_window.build()

    merchant = individual.Merchant()
    thread1 = merchant.buy()
    thread2 = merchant.sell()

    root.mainloop()


if __name__ == "__main__":
    main()