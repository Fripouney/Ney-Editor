import tkinter as tk
from file_handling import FileHandling

class MenuBarBuilder:
    """
    Service class to build the menu bar
    """
    def __init__(self, root: tk.Tk):
        self.root = root
        self.menu_bar = tk.Menu(self.root)

    def build(self):
        self.build_file_menu()
        self.build_insert_menu()
        return self.menu_bar

    def build_file_menu(self):
        """
        Method to build the "file" menu
        """
        menu = tk.Menu(self.root)
        menu.add_command(
            label="Nouveau", accelerator="Ctrl+N",
            command=lambda: FileHandling.new_file(self)
        )

        menu.add_command(
            label="Ouvrir", accelerator="Ctrl+O",
            command=lambda: FileHandling.open_file(self)
        )

        menu.add_separator()
        menu.add_command(
            label="Enregistrer", accelerator="Ctrl+S",
            command=lambda: FileHandling.save_file(self)
        )

        menu.add_command(
            label="Enregistrer sous", accelerator="Ctrl+Shift+S",
            command=lambda: FileHandling.save_as(self)
        )

        menu.add_separator()
        menu.add_command(label="Quitter", command=self.root.quit)
        
        self.menu_bar.add_cascade(label="Fichier", menu=menu)

    def build_insert_menu(self):
        """
        Method to build the "insert" menu
        """
        menu = tk.Menu(self.root)
        
        menu.add_command(
            label="Image...",
            command=lambda: FileHandling.insert_image(self)
        )
        self.menu_bar.add_cascade(label="Insertion", menu=menu)
