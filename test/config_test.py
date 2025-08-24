import pytest
import tkinter as tk
from config import Config

class TestConfig:
    root = tk.Tk()

    def test_add_text_area_bindings(self):
        text_area = tk.Text(self.root)
        text_area.pack()

        Config.add_text_area_bindings(text_area)

        assert text_area.bind() == ("<Control-Key-u>","<Control-Key-i>","<Control-Key-b>")

        self.root.destroy()
