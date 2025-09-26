import tkinter as tk
import base64
import io
from PIL import Image, ImageTk

class ImageInserter:
    """
    Service class to insert images into the text area
    """

    def __init__(self, text_area: tk.Text, image_source):
        self.text_area = text_area
        if isinstance(image_source, str):
            self.pil_image = Image.open(image_source)
            self.image_data = self.encode_to_base64(image_source)
            self.image = ImageTk.PhotoImage(file=image_source)
        elif isinstance(image_source, Image.Image):
            self.pil_image = image_source
            self.image_data = self.encode_pil_image_to_base64(image_source)
            self.image = ImageTk.PhotoImage(image_source)
        else:
            self.image = image_source
            self.image_data = None

    def insert_image(self):
        """
        Inserts the selected image in the text area at the current cursor position
        """
        cursor_index = self.text_area.index(tk.INSERT)
        self.text_area.image_create(cursor_index, image=self.image)
        return self.image_data

    def encode_to_base64(self, file_path: str) -> str:
        with open(file_path, "rb") as image_file:
            encoded = base64.b64encode(image_file.read()).decode("utf-8")
            return encoded
        
    def encode_pil_image_to_base64(self, pil_image) -> str:
        buffered = io.BytesIO()
        pil_image.save(buffered, format="PNG")
        encoded = base64.b64encode(buffered.getvalue()).decode("utf-8")
        return encoded
