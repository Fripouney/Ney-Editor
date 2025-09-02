import os
import tkinter as tk
import json
from tkinter import filedialog, messagebox
from utils import Utils
from service.file_opener import FileOpener
from service.error_handler import ErrorHandler

class FileHandling:
    """
    Class for handling file operations in the text editor
    """
    @staticmethod
    def save_file(editor, event=None):
        """
        Save the current file or prompt for a new file location if file has never been saved
        """
        if editor.current_file:
            if editor.current_file.endswith(".ney"):
                content = editor.text_area.dump(1.0, tk.END)
                content.pop(-1) # Remove the extra /n

                json_content = [
                    {"key": key, "value": value, "index": index}
                    for key, value, index in content
                ]
                with open(editor.current_file, 'w', encoding='utf-8') as file:
                    json.dump(json_content, file, indent=4)

            else:
                with open(editor.current_file, 'w', encoding='utf-8') as file:
                    file.write(editor.text_area.get(1.0, tk.END))

            Utils.set_status_bar(
                editor.status_bar,
                f"Fichier enregistré : {FileHandling.get_file_name(editor)}"
            )

        else:
            FileHandling.save_as(editor)

    @staticmethod
    def save_as(editor, event=None):
        """
        Prompt the user to select a file location to save the current file
        """
        file = filedialog.asksaveasfile(
            filetypes=[("Ney files", "*.ney"), ("Text files", "*.txt")],
        )
        if not file:
            return

        editor.current_file = file.name
        file.close()
        FileHandling.save_file(editor)
        editor.root.title(f"Ney editor - {FileHandling.get_file_name(editor)}")
        Utils.set_status_bar(
            editor.status_bar,
            f"Fichier enregistré : {FileHandling.get_file_name(editor)}"
        )

    @staticmethod
    def open_file(editor, filename=None, event=None):
        """
        Prompt the user to select a file to open
        Supported formats are .ney and .txt
        """
        if filename is None:
            file = filedialog.askopenfile(
                defaultextension=".ney",
                filetypes=[("Ney files", "*.ney"), ("Text files", "*.txt")],
                title="Ouvrir"
            )

            if not file:
                return
        else:
            try:
                file = open(filename, "r", encoding="utf-8")
            except FileNotFoundError:
                return

        if not FileHandling.is_valid_file_format(file.name):
            ErrorHandler.error_invalid_file_format(editor.status_bar)
            return

        if file.name is None:
            ErrorHandler.error_invalid_file_name(editor.status_bar)
            return

        editor.current_file = file.name

        FileOpener(file).open_file(editor)

        Utils.set_status_bar(
            editor.status_bar,
            f"Fichier ouvert : {FileHandling.get_file_name(editor)}"
        )
        editor.root.title(f"Ney editor - {FileHandling.get_file_name(editor)}")
        file.close()

    @staticmethod
    def new_file(editor, event=None):
        """
        Creates a brand new blank file.
        """
        confirm = messagebox.askyesno("Enregistrer ?", "Enregistrer les modifications ?")
        if confirm:
            FileHandling.save_file(editor)

        editor.text_area.delete(1.0, tk.END)
        editor.current_file = None
        editor.root.title("Ney Editor - Sans titre")

    @staticmethod
    def is_valid_file_format(file_name):
        """
        Check if the file format is valid
        """
        return file_name.endswith(".ney") or file_name.endswith(".txt")

    @staticmethod
    def get_file_name(editor):
        """
        Get the current file name without full path
        """
        return os.path.basename(editor.current_file) if editor.current_file else "Sans titre"
    
    @staticmethod
    def insert_image(editor, event=None):
        pass
