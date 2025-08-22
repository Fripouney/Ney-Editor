import tkinter as tk

class Util:
    @staticmethod
    def is_valid_file_format(file_name):
        return file_name.endswith(".ney") or file_name.endswith(".txt")
