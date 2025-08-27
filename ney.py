import tkinter as tk
from tkinter import ttk
from config import Config
from file_handling import FileHandling

class NeyEditor:
    """
    A text editor application for .ney and .txt files with formatting capabilities.

    This class builds the main window, text area, menu bar, and status bar,
    and provides file handling and text formatting features for editing and managing
    .ney and .txt files.
    """
    def __init__(self):
        """
        Initialize the main components of the editor
        """
        self.root = tk.Tk()
        self.text_area = tk.Text(self.root, font="Arial", wrap=tk.WORD, undo=True)
        self.status_bar = tk.Text(self.root, height=1, bd=0, bg="lightgrey", state="disabled")
        self.current_file = None

    def add_editor_bindings(self):
        """
        Add key bindings for the editor
        Currently supports:
        - Ctrl+S: Save
        - Ctrl+O: Open
        - Ctrl+Shift+S: Save As
        - Ctrl+N: New File
        """
        self.root.bind("<Control-s>", lambda event: FileHandling.save_file(self))
        self.root.bind("<Control-o>", lambda event: FileHandling.open_file(self))
        self.root.bind("<Control-S>", lambda event: FileHandling.save_as(self))
        self.root.bind("<Control-n>", lambda event: FileHandling.new_file(self))

    def build_root(self):
        """
        Build the root window for the editor
        """
        self.root.title(f"Ney Editor - {FileHandling.get_file_name(self)}")
        self.root.geometry("800x600")

    def build_menu_bar(self):
        """
        Build the top menu bar for the editor
        """
        menu_bar = tk.Menu(self.root)
        menu_bar.add_cascade(label="Fichier", menu=self.file_menu())
        self.root.config(menu=menu_bar)

    def build_toolbar(self):
        """
        Build the editor toolbar
        This will have buttons for bold, italic and underline
        """
        self.root.grid_rowconfigure(0, weight=0)
        self.root.grid_columnconfigure(0, weight=1)

        toolbar = tk.Frame(self.root, bd=1, relief=tk.RAISED)
        bold_btn = tk.Button(
            toolbar, text="B",
            command=lambda: Config.toggle_tag(self.text_area, "bold"),
            font=("Arial", 10, "bold")
        )
        italic_btn = tk.Button(
            toolbar, text="I",
            command=lambda: Config.toggle_tag(self.text_area, "italic"),
            font=("Arial", 10, "italic")
        )
        underline_btn = tk.Button(
            toolbar, text="U",
            command=lambda: Config.toggle_tag(self.text_area, "underline"),
            font=("Arial", 10, "underline")
        )
        bold_btn.pack(side=tk.LEFT, padx=2, pady=2)
        italic_btn.pack(side=tk.LEFT, padx=2, pady=2)
        underline_btn.pack(side=tk.LEFT, padx=2, pady=2)
        toolbar.grid(row=0, column=0, sticky="ew", columnspan=2)

    def build_text_area(self):
        """
        Build and configure the text area for the editor
        Also adds a scrollbar and configures text tags
        """

        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(1, weight=0)
        self.text_area.grid(row=1, column=0, sticky="nsew")
        scroll_bar = ttk.Scrollbar(self.root, command=self.text_area.yview)
        scroll_bar.grid(row=1, column=1, sticky="ns")
        self.text_area.configure(yscrollcommand=scroll_bar.set)

        Config.config_tags(self.text_area)
        Config.add_text_area_bindings(self.text_area)

    def build_status_bar(self):
        """
        Build the status bar for the editor
        """
        self.root.grid_rowconfigure(2, weight=0)
        self.status_bar.grid(row=2, column=0, columnspan=2, sticky="ew")

    def file_menu(self):
        """
        Build the file menu for the editor
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
        return menu

if __name__ == "__main__":
    editor = NeyEditor()
    editor.add_editor_bindings()
    editor.build_root()
    editor.build_menu_bar()
    editor.build_toolbar()
    editor.build_text_area()
    editor.build_status_bar()
    editor.root.mainloop()
