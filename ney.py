import json
import tkinter as tk
from tkinter import filedialog, messagebox
from util import Util
from config import Config

class NeyEditor:
    def __init__(self):
        self.root = tk.Tk()
        self.current_file = None

    def add_editor_bindings(self):
        self.root.bind("<Control-s>", self.save_file)
        self.root.bind("<Control-o>", self.open_file)
        self.root.bind("<Control-Shift-s>", self.save_as)
        self.root.bind("<Control-n>", self.new_file)

    def build_root(self):
        self.root.title("Ney Editor")
        self.root.geometry("800x600")

    def build_menu_bar(self):
        menu_bar = tk.Menu(self.root)
        menu_bar.add_cascade(label="Fichier", menu=self.file_menu())
        self.root.config(menu=menu_bar)

    def build_text_area(self):
        self.text_area = tk.Text(self.root, font="Arial")
        self.text_area.pack(expand=True, fill=tk.BOTH)
        Config.config_tags(self.text_area)
        Config.add_text_area_bindings(self.text_area)

    def build_status_bar(self):
        self.status_bar = tk.Text(self.root, height=1, bd=0, bg="lightgrey", state="disabled")
        self.status_bar.pack(fill=tk.X, side=tk.BOTTOM)

    def file_menu(self):
        menu = tk.Menu(self.root)
        menu.add_command(label="Nouveau", command=self.new_file)
        menu.add_command(label="Ouvrir", command=self.open_file)
        menu.add_separator()
        menu.add_command(label="Enregistrer", command=self.save_file)
        menu.add_command(label="Enregistrer sous", command=self.save_as)
        menu.add_separator()
        menu.add_command(label="Quitter", command=self.root.quit)
        return menu

    def save_file(self, event=None):
        if self.current_file:
            if self.current_file.endswith(".ney"):
                content = self.text_area.dump(1.0, tk.END, tag=True, text=True)
                
                json_content = [
                    {"key": key, "value": value, "index": index}
                    for key, value, index in content
                ]
                with open(self.current_file, 'w') as file:
                    json.dump(json_content, file, indent=4)

            else:
                with open(self.current_file, 'w') as file:
                    file.write(self.text_area.get(1.0, tk.END))

            Config.set_status_bar(self.status_bar,f"Fichier enregistré : {self.current_file}")

        else:
            self.save_as()

    def save_as(self, event=None):
        file = filedialog.asksaveasfile(
            defaultextension=".ney",
            filetypes=[("Ney files", "*.ney"), ("Text files", "*.txt")],
        )
        if not file:
            messagebox.showerror("Une erreur est survenue", "Le fichier n'a pas pu être enregistré !")
            Config.set_status_bar(self.status_bar, "ERREUR : Le fichier n'a pas pu être enregistré !")
            return
        
        self.current_file = file.name
        file.close()
        self.save_file()
        Config.set_status_bar(self.status_bar, f"Fichier enregistré : {self.current_file}")

    def open_file(self, event=None):
        file = filedialog.askopenfile(
            defaultextension=".ney",
            filetypes=[("Ney files", "*.ney"), ("Text files", "*.txt")],
            title="Ouvrir"
        )

        if not file:
            messagebox.showerror("Une erreur est survenue", "Le fichier n'a pas pu être ouvert !")
            Config.set_status_bar(self.status_bar, "ERREUR : Le fichier n'a pas pu être ouvert !")
            return

        self.text_area.delete(1.0, tk.END)
        self.current_file = file.name

        try:
            if not (Util.is_valid_file_format(self.current_file)):
                messagebox.showerror("Une erreur est survenue", "Le fichier n'est pas au format .ney ou .txt !")
                Config.set_status_bar(self.status_bar, "ERREUR : Le fichier n'est pas au format .ney ou .txt !")
                return

            if self.current_file.endswith(".ney"):
                content = json.load(file)
                content.sort(key=lambda item: item['key'] != 'text')

                print(content)  # Debug: Print loaded content
                for item in content:
                    key = item['key']
                    value = item['value']
                    index = item['index']
                    
                    if key == "text":
                        self.text_area.insert(index, value)
                    elif key == "tagon":
                        self.text_area.tag_add(value, index, tk.END)
                    elif key == "tagoff":
                        self.text_area.tag_remove(value, index, tk.END)

            else:
                content = file.read()
                self.text_area.insert(tk.END, content)

        except (json.JSONDecodeError, KeyError):
            messagebox.showerror("Erreur de lecture", "Le fichier .ney est corrompu ou mal formaté.")
            self.current_file = None

        finally:
            Config.set_status_bar(self.status_bar, f"Fichier ouvert : {self.current_file}")
            file.close()

    def new_file(self, event=None):
        confirm = messagebox.askyesno("Enregistrer ?", "Enregistrer les modifications ?")
        if confirm:
            self.save_file()
            
        self.text_area.delete(1.0, tk.END)
        self.current_file = None

if __name__ == "__main__":
    editor = NeyEditor()
    editor.add_editor_bindings()
    editor.build_root()
    editor.build_menu_bar()
    editor.build_text_area()
    editor.build_status_bar()

    editor.root.mainloop()