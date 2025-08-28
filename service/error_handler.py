from tkinter import messagebox
from config import Config

class ErrorHandler:
    """
    Class used to handle different errors when using the editor
    """
    @staticmethod
    def error_corrupt_file(status_bar):
        """
        Called when a .ney file is not properly formatted
        """
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
        """
        Called when user tries to open a file with an invalid format
        """
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
        """
        Called when a user tries to open a file with an incorrect name
        """
        messagebox.showerror(
            "Une erreur est survenue",
            "Le fichier n'a pas pu être ouvert (Nom incorrect)"
        )
        Config.set_status_bar(
            status_bar,
            "ERREUR : Le fichier n'a pas pu être ouvert (Nom incorrect)"
        )
