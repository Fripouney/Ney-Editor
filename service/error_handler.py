import tkinter as tk
from tkinter import messagebox
from config import Config

class ErrorHandler:
    @staticmethod
    def error_corrupt_file(status_bar):
        messagebox.showerror(
            "Erreur de lecture",
            "Le fichier .ney est corrompu ou mal formaté."
        )

        Config.set_status_bar(
            status_bar,
            "ERREUR : Le fichier .ney est corrompu ou mal formaté."
        )

    @staticmethod
    def error_invalid_file_format(status_bar):
        messagebox.showerror(
            "Une erreur est survenue",
            "Le fichier n'est pas au format .ney ou .txt !"
        )
        Config.set_status_bar(
            status_bar,
            "ERREUR : Le fichier n'est pas au format .ney ou .txt !"
        )

    @staticmethod
    def error_invalid_file_name(status_bar):
        messagebox.showerror(
            "Une erreur est survenue",
            "Le fichier n'a pas pu être ouvert (Nom incorrect)"
        )
        Config.set_status_bar(
            status_bar,
            "ERREUR : Le fichier n'a pas pu être ouvert (Nom incorrect)"
        )