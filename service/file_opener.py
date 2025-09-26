import tkinter as tk
import json
import base64
import io
from PIL import Image, ImageTk
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

                case "image":
                    self.insert_image_from_b64(editor, value, index)


    def handle_tags(self, editor, value, index):
        """
        Configures and applies tags in the text area
        """
        if value not in editor.text_area.tag_names(index):
            TextFormatter.toggle_tag(editor.text_area, value, index)

    def handle_txt_file(self, editor):
        """
        Reads and displays the content of the .txt file
        """
        content = self.file.read()
        editor.text_area.delete(1.0, tk.END)
        editor.text_area.insert(tk.END, content)

    def insert_image_from_b64(self, editor, b64_data, index):
        """
        Decodes base64 image data and inserts the image at index
        """
        try:
            image_bytes = base64.b64decode(b64_data)
            image = Image.open(io.BytesIO(image_bytes))
            photo_image = ImageTk.PhotoImage(image)
            editor.image_references.append(photo_image)
            editor.image_data_map.append(b64_data)
            editor.text_area.image_create(index, image=photo_image)
        except Exception as e:
            ErrorHandler.error_image_load(editor.status_bar)
            print(f"Error loading image: {e}")
