import tkinter as tk
import json
from service.error_handler import ErrorHandler
from service.text_formatter import TextFormatter

class FileOpener:
    """
    Service class to open and parse .ney and .txt files
    """
    def __init__(self, file):
        self.file = file


    def open_file(self, editor):
        """
        Opens the selected file
        """
        if self.file.name.endswith(".ney"):
            self.handle_ney_file(editor)
        else:
            self.handle_txt_file(editor)


    def handle_ney_file(self, editor):
        """
        Parses the content of the .ney file and displays it
        """
        try:
            content = json.load(self.file)
        except json.JSONDecodeError:
            ErrorHandler.error_corrupt_file(editor.status_bar)
            return
        content.sort(key=lambda item: item['key'] != 'text')
        editor.text_area.delete(1.0, tk.END)
        for item in content:
            key = item['key']
            value = item['value']
            index = item['index']

            match key:
                case "text":
                    editor.text_area.insert(index, value)

                case "tagon":
                    self.handle_tags(editor, value, index)

                case "tagoff":
                    editor.text_area.tag_remove(value, index, tk.END)


    def handle_tags(self, editor, value, index):
        """
        Configures and applies tags in the text area
        """
        if value not in editor.text_area.tag_names():
            TextFormatter.toggle_tag(editor.text_area, value, index)

    def handle_txt_file(self, editor):
        """
        Reads and displays the content of the .txt file
        """
        content = self.file.read()
        editor.text_area.delete(1.0, tk.END)
        editor.text_area.insert(tk.END, content)
