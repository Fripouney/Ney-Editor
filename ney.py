import tkinter as tk
from tkinter import ttk
from sys import argv
from config import Config
from file_handling import FileHandling
from service.text_formatter import TextFormatter
from service.menu_bar_builder import MenuBarBuilder

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

    def build_root(self):
        """
        Build the root window for the editor
        """
        self.root.title(f"Ney Editor - {FileHandling.get_file_name(self)}")
        self.root.geometry("800x600")
        Config.add_editor_bindings(self)

    def build_menu_bar(self):
        """
        Build the top menu bar for the editor
        """
        menu_bar = MenuBarBuilder(self.root).build()
        self.root.config(menu=menu_bar)

    def build_toolbar(self):
        """
        Build the editor toolbar
        This will have buttons for bold, italic, underline and text color
        """
        self.root.grid_rowconfigure(0, weight=0)
        self.root.grid_columnconfigure(0, weight=1)

        toolbar = tk.Frame(self.root, bd=1, relief=tk.RAISED)
        bold_btn = tk.Button(
            toolbar, text="B",
            command=lambda: TextFormatter.toggle_tag(self.text_area, "bold"),
            font=("Arial", 10, "bold")
        )

        italic_btn = tk.Button(
            toolbar, text="I",
            command=lambda: TextFormatter.toggle_tag(self.text_area, "italic"),
            font=("Arial", 10, "italic")
        )

        underline_btn = tk.Button(
            toolbar, text="U",
            command=lambda: TextFormatter.toggle_tag(self.text_area, "underline"),
            font=("Arial", 10, "underline")
        )

        color_btn = tk.Button(
            toolbar, text="Color",
            command=lambda: TextFormatter.change_text_color(self)
        )

        possible_sizes = ("8", "10", "12", "14", "16", "18", "20")
        size_menu = tk.OptionMenu(
            toolbar,
            tk.StringVar(value="Taille"),
            *possible_sizes,
            command=lambda size: TextFormatter.toggle_tag(self.text_area, f"size_{size}")
        )

        bold_btn.pack(side=tk.LEFT, padx=2, pady=2)
        italic_btn.pack(side=tk.LEFT, padx=2, pady=2)
        underline_btn.pack(side=tk.LEFT, padx=2, pady=2)
        color_btn.pack(side=tk.LEFT, padx=2, pady=2)
        size_menu.pack(side=tk.LEFT, padx=2, pady=2)
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

        # Config.config_tags(self.text_area)
        Config.add_text_area_bindings(self.text_area)

    def build_status_bar(self):
        """
        Build the status bar for the editor
        """
        self.root.grid_rowconfigure(2, weight=0)
        self.status_bar.grid(row=2, column=0, columnspan=2, sticky="ew")


if __name__ == "__main__":
    editor = NeyEditor()
    editor.build_root()
    editor.build_menu_bar()
    editor.build_toolbar()
    editor.build_text_area()
    editor.build_status_bar()

    if len(argv) > 1:
        FileHandling.open_file(editor, argv[1])

    editor.root.mainloop()
