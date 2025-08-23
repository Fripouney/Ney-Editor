import json
from tkinter import filedialog, messagebox
from config import Config
from util import Util
import tkinter as tk

class FileHandling:
    @staticmethod
    def save_file(editor, event=None):
        if editor.current_file:
            if editor.current_file.endswith(".ney"):
                content = editor.text_area.dump(1.0, tk.END, tag=True, text=True)
                
                json_content = [
                    {"key": key, "value": value, "index": index}
                    for key, value, index in content
                ]
                with open(editor.current_file, 'w') as file:
                    json.dump(json_content, file, indent=4)

            else:
                with open(editor.current_file, 'w') as file:
                    file.write(editor.text_area.get(1.0, tk.END))

            Config.set_status_bar(editor.status_bar,f"Fichier enregistré : {editor.current_file}")

        else:
            editor.save_as()

    @staticmethod
    def save_as(editor, event=None):
        file = filedialog.asksaveasfile(
            defaultextension=".ney",
            filetypes=[("Ney files", "*.ney"), ("Text files", "*.txt")],
        )
        if not file:
            messagebox.showerror("Une erreur est survenue", "Le fichier n'a pas pu être enregistré !")
            Config.set_status_bar(editor.status_bar, "ERREUR : Le fichier n'a pas pu être enregistré !")
            return

        editor.current_file = file.name
        file.close()
        FileHandling.save_file(editor)
        Config.set_status_bar(editor.status_bar, f"Fichier enregistré : {editor.current_file}")

    @staticmethod
    def open_file(editor, event=None):
        file = filedialog.askopenfile(
            defaultextension=".ney",
            filetypes=[("Ney files", "*.ney"), ("Text files", "*.txt")],
            title="Ouvrir"
        )

        if not file:
            messagebox.showerror("Une erreur est survenue", "Le fichier n'a pas pu être ouvert !")
            Config.set_status_bar(editor.status_bar, "ERREUR : Le fichier n'a pas pu être ouvert !")
            return

        editor.text_area.delete(1.0, tk.END)
        editor.current_file = file.name

        try:
            if not (Util.is_valid_file_format(editor.current_file)):
                messagebox.showerror("Une erreur est survenue", "Le fichier n'est pas au format .ney ou .txt !")
                Config.set_status_bar(editor.status_bar, "ERREUR : Le fichier n'est pas au format .ney ou .txt !")
                return

            if editor.current_file.endswith(".ney"):
                content = json.load(file)
                content.sort(key=lambda item: item['key'] != 'text')

                for item in content:
                    key = item['key']
                    value = item['value']
                    index = item['index']
                    
                    if key == "text":
                        editor.text_area.insert(index, value)
                    elif key == "tagon":
                        editor.text_area.tag_add(value, index, tk.END)
                    elif key == "tagoff":
                        editor.text_area.tag_remove(value, index, tk.END)

            else:
                content = file.read()
                editor.text_area.insert(tk.END, content)

        except (json.JSONDecodeError, KeyError):
            messagebox.showerror("Erreur de lecture", "Le fichier .ney est corrompu ou mal formaté.")
            editor.current_file = None

        finally:
            Config.set_status_bar(editor.status_bar, f"Fichier ouvert : {editor.current_file}")
            file.close()

    @staticmethod
    def new_file(editor, event=None):
        confirm = messagebox.askyesno("Enregistrer ?", "Enregistrer les modifications ?")
        if confirm:
            FileHandling.save_file(editor)

        editor.text_area.delete(1.0, tk.END)
        editor.current_file = None