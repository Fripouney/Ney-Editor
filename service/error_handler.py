from tkinter import messagebox
from utils import Utils

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

        Utils.set_status_bar(
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
        Utils.set_status_bar(
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
        Utils.set_status_bar(
            status_bar,
            "ERREUR : Le fichier n'a pas pu être ouvert (Nom incorrect)"
        )

    @staticmethod
    def error_image_load(status_bar):
        """
        Called when an image fails to load
        """
        messagebox.showerror(
            "Erreur de chargement de l'image",
            "L'image n'a pas pu être chargée."
        )
        Utils.set_status_bar(
            status_bar,
            "ERREUR : L'image n'a pas pu être chargée."
        )
