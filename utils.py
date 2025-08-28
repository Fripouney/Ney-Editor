import tkinter as tk

class Utils:
    @staticmethod
    def set_status_bar(status_bar, text):
        """
        Set the text of the status bar
        """
        status_bar.config(state="normal")
        status_bar.delete(1.0, tk.END)
        status_bar.insert(tk.END, text)
        status_bar.config(state="disabled")