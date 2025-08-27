import os
import tkinter as tk
import json
from tkinter import filedialog, messagebox
from config import Config

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
                content = editor.text_area.dump(1.0, tk.END, tag=True, text=True)
                content.pop(-1) # Remove the extra /n

                json_content = [
                    {"key": key, "value": value, "index": index}
                    for key, value, index in content
                ]
                with open(editor.current_file, 'w') as file:
                    json.dump(json_content, file, indent=4)

            else:
                with open(editor.current_file, 'w') as file:
                    file.write(editor.text_area.get(1.0, tk.END))

            Config.set_status_bar(
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
        Config.set_status_bar(
            editor.status_bar,
            f"Fichier enregistré : {FileHandling.get_file_name(editor)}"
        )

    @staticmethod
    def open_file(editor, event=None):
        """
        Prompt the user to select a file to open
        Supported formats are .ney and .txt
        """
        file = filedialog.askopenfile(
            defaultextension=".ney",
            filetypes=[("Ney files", "*.ney"), ("Text files", "*.txt")],
            title="Ouvrir"
        )

        if not file:
            return

        if not FileHandling.is_valid_file_format(file.name):
            messagebox.showerror(
                "Une erreur est survenue",
                "Le fichier n'est pas au format .ney ou .txt !"
            )
            Config.set_status_bar(
                editor.status_bar,
                "ERREUR : Le fichier n'est pas au format .ney ou .txt !"
            )
            return

        if file.name is None:
            messagebox.showerror(
                "Une erreur est survenue",
                "Le fichier n'a pas pu être ouvert (Nom incorrect)"
            )
            Config.set_status_bar(
                editor.status_bar,
                "ERREUR : Le fichier n'a pas pu être ouvert (Nom incorrect)"
            )
            return

        editor.current_file = file.name

        if editor.current_file.endswith(".ney"):
            try:
                content = json.load(file)
                content.sort(key=lambda item: item['key'] != 'text')
                editor.text_area.delete(1.0, tk.END)

                for item in content:
                    key = item['key']
                    value = item['value']
                    index = item['index']

                    if key == "text":
                        editor.text_area.insert(index, value)
                    elif key == "tagon":
                        if not value in editor.text_area.tag_names():
                            splitted_value = value.split("_")
                            match splitted_value[0]:
                                case "color":
                                    editor.text_area.tag_configure(value, foreground=splitted_value[1])
                                case _:
                                    editor.text_area.tag_configure(value)
                        
                        editor.text_area.tag_add(value, index, tk.END)
                    elif key == "tagoff":
                        editor.text_area.tag_remove(value, index, tk.END)

            except (json.JSONDecodeError, KeyError):
                messagebox.showerror(
                    "Erreur de lecture",
                    "Le fichier .ney est corrompu ou mal formaté."
                )
                editor.current_file = None
                return

        else:
            content = file.read()
            editor.text_area.delete(1.0, tk.END)
            editor.text_area.insert(tk.END, content)

        Config.set_status_bar(
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
