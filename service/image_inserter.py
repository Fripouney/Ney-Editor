import tkinter as tk
from PIL import ImageTk

class ImageInserter:
    """
    Service class to insert images into the text area
    """

    def __init__(self, text_area: tk.Text, image: ImageTk.PhotoImage):
        self.text_area = text_area
        self.image = image

    def insert_image(self):
        """
        Inserts the selected image in the text area at the current cursor position
        """
        cursor_index = self.text_area.index(tk.INSERT)
        self.text_area.image_create(cursor_index, image=self.image)
