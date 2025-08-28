import tkinter as tk
from file_handling import FileHandling
from service.text_formatter import TextFormatter

class Config:
    """
    Configuration for different components of the editor
    """
    @staticmethod
    def add_editor_bindings(editor):
        """
        Add key bindings for the editor
        Currently supports:
        - Ctrl+S: Save
        - Ctrl+O: Open
        - Ctrl+Shift+S: Save As
        - Ctrl+N: New File
        """
        editor.root.bind("<Control-s>", lambda event: FileHandling.save_file(editor))
        editor.root.bind("<Control-o>", lambda event: FileHandling.open_file(editor))
        editor.root.bind("<Control-S>", lambda event: FileHandling.save_as(editor))
        editor.root.bind("<Control-n>", lambda event: FileHandling.new_file(editor))

    @staticmethod
    def add_text_area_bindings(text_area):
        """
        Add key bindings for text formatting in the text area
        """
        text_area.bind("<Control-b>", lambda event: TextFormatter.toggle_tag(text_area, "bold"))
        text_area.bind("<Control-i>", lambda event: TextFormatter.toggle_tag(text_area, "italic"))
        text_area.bind("<Control-u>", lambda event: TextFormatter.toggle_tag(text_area, "underline"))

    # @staticmethod
    # def config_tags(text_area):
    #     """
    #     Configure text area tags for the editor
    #     """
    #     text_area.tag_configure("bold", font=("Arial", 12, "bold"))
    #     text_area.tag_configure("italic", font=("Arial", 12, "italic"))
    #     text_area.tag_configure("underline", font=("Arial", 12, "underline"))

    # @staticmethod
    # def toggle_tag(text_area, tag, event=None):
    #     """
    #     Toggle a text area tag on the selected text
    #     """
    #     try:
    #         current_tags = text_area.tag_names("sel.first")
    #         if tag in current_tags:
    #             text_area.tag_remove(tag, "sel.first", "sel.last")
    #         else:
    #             text_area.tag_add(tag, "sel.first", "sel.last")
    #     except tk.TclError:
    #         print("No text selected to toggle tag.")

    #     return "break"
